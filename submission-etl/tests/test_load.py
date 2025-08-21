import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from utils.load import save_to_csv, save_to_postgresql

class TestLoad(unittest.TestCase):

    def test_save_to_csv(self):
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        with patch('pandas.DataFrame.to_csv') as mock_to_csv:
            save_to_csv(df, "dummy.csv")
            mock_to_csv.assert_called_once_with("dummy.csv", index=False)

    @patch('utils.load.create_engine')
    def test_save_to_postgresql_berhasil(self, mock_create_engine):
        df = pd.DataFrame({'col1': [1], 'col2': [2]})
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine
        
        with patch.object(df, 'to_sql') as mock_to_sql, patch('builtins.print') as mock_print:
            save_to_postgresql(df, 'goods')
            
            mock_create_engine.assert_called_once_with(
                'postgresql+psycopg2://postgres:77apaya@localhost:5432/etldb'
            )
            
            mock_to_sql.assert_called_once_with('goods', mock_engine, if_exists='replace', index=False)
            mock_print.assert_called_with("Data berhasil disimpan ke PostgreSQL, tabel: 'goods'")

    @patch('utils.load.create_engine')
    def test_save_to_postgresql_gagal(self, mock_create_engine):
        df = pd.DataFrame({'col1': [1]})
        mock_create_engine.side_effect = Exception("Koneksi gagal")

        with patch('builtins.print') as mock_print:
            save_to_postgresql(df, 'goods')
            printed_messages = [call_args[0][0] for call_args in mock_print.call_args_list]
            self.assertTrue(any("Gagal menyimpan data ke PostgreSQL" in msg for msg in printed_messages))

if __name__ == '__main__':
    unittest.main()
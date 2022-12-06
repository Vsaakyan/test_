import unittest
from unittest.mock import patch, Mock
import main


class Test_funk(unittest.TestCase):
    def setUp(self) -> None:
        print("setup START")

    def tearDown(self) -> None:
        print ('tearDown  STOP')

    def test_check_document_existance_True(self):
        result = main.check_document_existance('11-2')
        self.assertEqual(result, True)

    def test_check_document_existance_Falce(self):
        result = main.check_document_existance('noname')
        self.assertEqual(result, False)

    @patch('builtins.input', return_value='11-2')
    def test_get_doc_owner_name(self, input):
        self.assertEqual(main.get_doc_owner_name(), "Геннадий Покемонов")

    def test_get_all_doc_owners_names(self):
        self.assertIn('Василий Гупкин', main.get_all_doc_owners_names())

    def test_remove_doc_from_shelf(self):
        self.assertNotIn('11-2', main.remove_doc_from_shelf('11-2'))

    @patch('builtins.input', return_value='3e')
    def test_add_new_shelf(self, input):
        self.assertEqual(main.add_new_shelf(), ('3e', True))

    def test_append_doc_to_shelf(self):
        self.assertIn('33965', main.append_doc_to_shelf('33965', '3')['3'])

    @patch('builtins.input', return_value='10006')
    def test_delete_doc(self, input):
        self.assertEqual(main.delete_doc(), ('10006', True))

    @patch('builtins.input', return_value='11-2')
    def test_get_doc_shelf(self, input):
        self.assertEqual(main.get_doc_shelf(), ('1'))

    @patch('builtins.input', side_effect=['11-2', '3'])
    def test_move_doc_to_shelf(self, mock_input):
        user_doc_number = mock_input
        user_shelf_number = mock_input
        self.assertEqual(main.move_doc_to_shelf(), ('11-2', '3') )

    @patch('builtins.input', side_effect=['222', 'drive_lic', 'Sergey', '3'])
    def test_add_new_doc(self, mock_input):
        new_doc_number = mock_input
        new_doc_type = mock_input
        new_doc_owner_name = mock_input
        new_doc_shelf_number = mock_input
        self.assertEqual(main.add_new_doc(), ('3'))
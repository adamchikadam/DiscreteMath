import unittest
from huffman import huffman_encoding, huffman_decoding, build_huffman_codes

class TestHuffmanEncoding(unittest.TestCase):

    def test_empty_string(self):
        encoded_text, codes = huffman_encoding("")
        self.assertEqual(encoded_text, "")
        self.assertEqual(codes, {})


    def test_simple_string(self):
        text = "BaaBa"
        encoded_text, codes = huffman_encoding(text)
        self.assertEqual(huffman_decoding(encoded_text, codes), text)

    def test_longer_string(self):
        text = "Пример дерева Хаффмана"
        encoded_text, codes = huffman_encoding(text)
        self.assertEqual(huffman_decoding(encoded_text, codes), text)

    def test_string_with_numbers(self):
        text = "abc123abc"
        encoded_text, codes = huffman_encoding(text)
        self.assertEqual(huffman_decoding(encoded_text, codes), text)

    def test_correct_huffman_codes(self):
        text = "aaaaabbbbcccdd"
        encoded_text, codes = huffman_encoding(text)

        self.assertTrue(len(codes['a']) <= len(codes['b']))
        self.assertTrue(len(codes['b']) <= len(codes['c']))
        self.assertTrue(len(codes['c']) <= len(codes['d']))

        self.assertEqual(huffman_decoding(encoded_text, codes), text)

    def test_build_huffman_codes_function(self):
        text = "hello world"
        codes = build_huffman_codes(text)
        self.assertIsInstance(codes, dict)
        self.assertTrue(all(isinstance(code, str) for code in codes.values()))


if __name__ == '__main__':
    unittest.main()
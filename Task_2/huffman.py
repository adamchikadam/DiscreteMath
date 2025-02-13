from collections import Counter
import heapq

def build_huffman_codes(text):
    # Проверка, что текст не пустой
    if not text:
        return {}

    frequencies = Counter(text)

    # 1. Создание очереди
    heap = [[weight, [char, ""]] for char, weight in frequencies.items()]
    heapq.heapify(heap)

    # 2. Построение дерева и кодов
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
            # Присваиваем 0 левым ветвям
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
            # Присваиваем 1 правым ветвям
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # 3. Возвращаем коды, отсортировка по символам
    return {char: code for char, code in sorted(heapq.heappop(heap)[1:], key=lambda p: p[0])}

def huffman_encoding(text):
    # Кодировка с использованием кодов Хаффмана
    codes = build_huffman_codes(text)
    if not codes:
        return "", codes
    encoded_text = ''.join(codes[char] for char in text)
    return encoded_text, codes

def huffman_decoding(encoded_text, codes):
    if not codes:
        return ""
    reverse_codes = {code: char for char, code in codes.items()}
    decoded_text = ''
    current_code = ''
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ''
    return decoded_text


if __name__ == "__main__":
    print("--- Кодирование и декодирование Хаффмана ---")

    # Запрос текста у пользователя
    user_text = input("Введите текст для кодирования: ")

    # Кодируем и декодируем текст
    encoded_text, codes = huffman_encoding(user_text)
    decoded_text = huffman_decoding(encoded_text, codes)

    # Вывод результатов
    print(f"Текст: {user_text}")
    print(f"Коды Хаффмана: {codes}")
    print(f"Закодированный текст: {encoded_text}")
    print(f"Декодированный текст: {decoded_text}")
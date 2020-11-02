from secrets import token_bytes

# XOR encryption using one time pad system
def encryption(mess):
    def random_key(length):
        # Creates length random bits and returns it as a big endian integer
        tb = token_bytes(length)
        return int.from_bytes(tb, "big")

    def encrypt(original):
        original_bytes = original.encode()  # make bytes
        dummy = random_key(len(original_bytes))
        original_key = int.from_bytes(original_bytes, "big")  # Transfers bytes to int
        encrypted = original_key ^ dummy  # ^ is XOR
        return dummy, encrypted

    def decrypt(key1, key2):
        decrypted = key1 ^ key2
        # Note: adding 7 ensures that we round up
        temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
        return temp.decode()

    key1, key2 = encrypt(mess)
    result = decrypt(key1, key2)
    print(result)

encryption("This is a test message.")

    


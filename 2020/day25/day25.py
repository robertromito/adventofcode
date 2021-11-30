SUBJECT_NUMBER_DIVISOR = 20201227

card_subject_number = 7
card_public_key = 19774466
door_subject_number = 7
door_public_key = 7290641

def transform_subject_number(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= SUBJECT_NUMBER_DIVISOR
    return value

def get_loop_size(public_key, subject_number):
    loop_size = 0
    value = 1
    while True:
        loop_size += 1
        value *= subject_number
        value %= SUBJECT_NUMBER_DIVISOR
        if value == public_key:
            return loop_size

print("="*25)
print("Determining card loop size")
card_loop_size = get_loop_size(card_public_key, card_subject_number)
print(f"Card loop size is {card_loop_size}")

print("Determining door loop size")
door_loop_size = get_loop_size(door_public_key, door_subject_number)
print(f"Door loop size is {door_loop_size}")

print("Determining encryption key from card")
card_encryption_key = transform_subject_number(door_public_key, card_loop_size)
print(f"Card encryption key is {card_encryption_key}")

print("Determining encryption key from door")
door_encryption_key = transform_subject_number(card_public_key, door_loop_size)
print(f"Door encryption key is {door_encryption_key}")


import random

secret_pin = input("Enter your pin: ")# ဒါကတော့ ခိုးရမယ့် PIN နံပါတ်
guess = ""
attempts = 0

while guess != secret_pin:
    # ကွန်ပျူတာက 0000 ကနေ 9999 ထိ ခန့်မှန်းနေတာကို ပြချင်လို့ပါ
    guess = str(random.randint(1000, 9999))
    attempts += 1

print(f"Hacker က {attempts} ကြိမ်မြောက်မှာ PIN နံပါတ်ကို သိသွားပါပြီ!")

# စာလုံးတွေကို ၃ လုံးစီ ရှေ့တိုးပြီး လျှို့ဝှက်စာလုပ်မယ်
message = input("ပြောင်းချင်သော စာသား ရိုက်ထည့်ပါ: ")
secret_message = ""

for letter in message:
    # ASCII value ကိုသုံးပြီး အက္ခရာကို ပြောင်းတာပါ
    new_char = chr(ord(letter) + 3)
    secret_message += new_char

print("လျှို့ဝှက်စာသားမှာ -", secret_message)
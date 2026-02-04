password = input("စစ်ဆေးမယ့် Password ကို ရိုက်ထည့်ပါ: ")

if len(password) < 8:
    print("❌ အရမ်းတိုလွန်းတယ်! အနည်းဆုံး ၈ လုံး ရှိရမယ်။")
elif password.isalpha():
    print("⚠️ ဂဏန်းတွေလည်း ထည့်သင့်တယ်နော်။")
else:
    print("✅ ဒါကတော့ အားကောင်းတဲ့ Password ပါ!")
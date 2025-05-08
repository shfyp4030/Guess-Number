import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("به بازی حدس عدد خوش اومدی!")
    print("یه عدد بین 1 تا 100 حدس بزن.")
    
    while True:
        try:
            guess = int(input("حدست چیه؟ "))
            attempts += 1
            
            if guess < 1 or guess > 100:
                print("لطفاً عددی بین 1 تا 100 وارد کن!")
                continue
                
            if guess < secret_number:
                print("حدست خیلی کمه! دوباره سعی کن.")
            elif guess > secret_number:
                print("حدست خیلی بالاست! دوباره سعی کن.")
            else:
                print(f"آفرین! عدد درست {secret_number} بود!")
                print(f"تعداد تلاش‌ها: {attempts}")
                break
                
        except ValueError:
            print("لطفاً یه عدد معتبر وارد کن!")
    
    again = input("دوباره بازی کن؟ (بله/خیر): ")
    if again.lower() == "بله":
        guess_number()
    else:
        print("مرسی که بازی کردی! خداحافظ!")

guess_number()

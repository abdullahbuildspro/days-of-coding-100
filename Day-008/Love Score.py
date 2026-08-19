
def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()   # هنا لنحول كل الحروف الى حروف صغيرة حتى لا يفرق الكمبيوتر بينهم ودمج بين الاسمين لان المهم عندي كم عدد حروف true و love في الاسمين مع بعض

    true_count = 0
    for letter in "true":  # يدخل كلمة true في المتغير مش يدير اللي نبيه بعد شوي
        true_count += combined_names.count(letter)  # true_countحط عدد مرات ظهور الحرف في المتغير combined_names ثم العدد أدخله في المتغير

# combined_names فيها الاسمين الذين نريد معرفة العلاقة بينهم
# letterفيها الحروف التي نبحث عنها
# نبحث عن كلمة true و love
# .count  تعطيك عدد مرات وجود هذا الحرف في الكلمة

    love_count = 0
    for letter in "love":
        love_count += combined_names.count(letter)

    love_score = int(str(true_count) + str(love_count)) # نحن لا نريد الجمع بينهم كأرقام، بل نريد أن يضعهم جنب بعض فيلزم أن نجعلهم حروف حتى تكون جنب بعض، ثم نحولهم الى ارقام

# str() للتحويل الى صيغة حروف
# int() للتحويل الى صيغة أرقام

    print(f"Love Score = {love_score}")

calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer")

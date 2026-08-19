
from prettytable import PrettyTable  # استدعاء لمكتبة الجداول

# الـ PrettyTable هي الـ Class
table = PrettyTable()
table2 = PrettyTable()

# هنا أول جدول، سيكون الاثنين جنب بعض، كل كلمة من الجدول ستقابل الكلمة من الجدول الثاني بالترتيب
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# إذا أردت إضافة جدول آخر تحت الجدول الأول
table2.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table2.add_column("Type", ["Electric", "Water", "Fire"])

# # هنا نقوم بمحاذاة الكلام في الجدول، اكتب "r" إذا أردت المحاذاة إلى اليمين، واكتب "l" إذا أردت المحاذاة إلى اليسار، واكتب "c" إذا أردت المحاذاة إلى الوسط
table.align = "r"

print(table)
print(table2)
import Rhino.Geometry as rg
import random

# المدخلات المطلوبة في Grasshopper:
# spacing (رقم للتباعد)
# height_variation (رقم لمدى التفاوت)

points = []
# بناء شبكة نقاط أساسية
for i in range(10):
    for j in range(10):
        # إزاحة عشوائية للارتفاع لدعم الفكر التفكيكي
        z = random.uniform(0, height_variation)
        pt = rg.Point3d(i * spacing, j * spacing, z)
        points.append(pt)

lines = []
# توصيل النقاط لإنشاء تكوين شبكي
for i in range(len(points)-1):
    # نسبة عشوائية لكسر النمطية المعتادة
    if random.random() > 0.4:
        line = rg.Line(points[i], points[i+1])
        lines.append(line)

# المخرج النهائي (Output):
a = lines

import numpy as np
import pandas as pd
print("________________________________МЕТОД ВАЛЬДА___________________________________________")

orig_array = np.array([
         [20, 25, 15],
         [25, 24, 10],
         [15, 28, 12],
         [9, 30, 20]])

wald_rows = np.amax(orig_array, 1)
wald_ans = wald_rows.min()
wald_index = np.where(orig_array == wald_ans)
print("Используя метод Вальда наиболее выгодной является стратегия содерержащая элемент: " , wald_ans)
print("Стратегии содержащие элементы по Вальду располагаются в матрице по индексам: ", wald_index )

print('\t')
print("________________________________МЕТОД СЕВИДЖА___________________________________________")

mod_array = np.array([[11, 1, 5],
                      [16, 0, 0],
                      [6, 4, 2],
                      [0, 6, 10]])
sev_rows = np.max(mod_array, 1)
sev_ans = sev_rows.min()
sev_index = np.where(sev_rows == sev_rows.min())
print("Используя метод Севиджа наиболее выгодной является стратегия содерержащая элемент: " , sev_ans)
print("Стратегии содержащие элементы по Севиджу располагаются в матрице по индексам: ", sev_index )

print('\t')
print("________________________________МЕТОД ГУРВИЦА___________________________________________")

gur_rows_max_A = np.max(orig_array, 1)
gur_rows_min_A = np.min(orig_array, 1)
gur_rows_max_R = np.max(mod_array, 1)
gur_rows_min_R = np.min(mod_array, 1)

gur_ans_all_A = (((gur_rows_max_A)*0.9) + ((gur_rows_min_A)*0.1))
gur_ans_all_R = (((gur_rows_max_R)*0.1) + ((gur_rows_min_R)*0.9))

gur_ans_A = np.min(((gur_rows_max_A)*0.9) + ((gur_rows_min_A)*0.1))
index_A = np.where(gur_ans_A == gur_ans_all_A)

gur_ans_R = np.min(((gur_rows_max_R)*0.1) + ((gur_rows_min_R)*0.9))
index_R = np.where(gur_ans_R == gur_ans_all_R)

print("Используя метод Гурвица наиболее выгодной является стратегия чья сумма по формуле равна: " , gur_ans_A,"при работе с изначальной матрицей")
print("Используя метод Гурвица наиболее выгодной является стратегия чья сумма по формуле равна: " , gur_ans_R,"при работе с модифицированной матрицей")
print('\t')
print("Стратегии по Гурвицу располагаются в матрице по индексам(оригинальной матрицы): ", index_A )
print("Стратегии по Гурвицу располагаются в матрице по индексам(модифицированной матрицы): ", index_R )


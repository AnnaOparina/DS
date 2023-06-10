money = int(input("Введите сумму, которую желаете вложить: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
procent = list(per_cent.values())
print('Процентная ставка',procent)
TKB = int(money * procent[0]/100)
CKB = int(money * procent[1]/100)
VTB = int(money * procent[2]/100)
Sber = int(money * procent[3]/100)
Deposit=[TKB, CKB, VTB, Sber]
print('Возможный доход',Deposit)
Deposit.sort(reverse=True)
print('Максимальная сумма которую вы можете заработать- ',Deposit[0])
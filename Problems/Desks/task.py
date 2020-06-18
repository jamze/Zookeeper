ppl_1=int(input())
ppl_2=int(input())
ppl_3=int(input())

desk_1_add=ppl_1%2
desk_1=int(ppl_1/2)

desk_2_add=ppl_2%2
desk_2=int(ppl_2/2)

desk_3_add=ppl_3%2
desk_3=int(ppl_3/2)

total_desks=desk_1+desk_1_add+desk_2+desk_2_add+desk_3+desk_3_add
print(total_desks)
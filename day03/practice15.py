"""
    对折多少次
"""
paper_ply= 0.01
collapse = 0
while paper_ply<8844430:
    paper_ply *= 2
    collapse+=1

print(collapse)
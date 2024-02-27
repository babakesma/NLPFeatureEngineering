# Two consequent sentences send to function to extract the cause and effects of texts 
# No Specific library needs
def search_for_cause_effect(text,former_sentence):
    #print("Cause and effect hase been searched for:")
    #print(text)
    cause=''
    effect=''
    if text.find('; therefore,')>-1:
        print(1)
        index1 = text.find('; therefore,')
        cause=text[: index1 ].strip().split(" and ")
        effect=text[index1+13:]
    elif text.find(' will mean ')>-1:
        print(2)
        index1= text.find(' will mean ')
        cause=text[: index1 ].strip().split(" and ")
        effect=text[index1+11:]
    elif text.find(' because ')>-1:
        print(2)
        index1= text.find(' because ')
        effect=text[: index1 ]
        cause=text[index1+9:].strip().split(" and ")
    elif text.find(" it mean's ")>-1:
        print(3)
        index1= text.find(" it mean's ")
        cause=text[: index1 ].strip().split(" and ")
        effect=text[index1+11:]
    elif text.find(" lead to ")>-1:
        print(4)
        index1= text.find(" lead to ")
        cause=text[: index1 ].strip().split(" and ")
        effect=text[index1+9:]
    elif text.find(" has led to ")>-1:
        print(5)
        index1= text.find(" has led to ")
        print(index1)
        cause=text[ :index1].strip().split(", and ")
        effect=text[index1+12: ]
    elif text.find(" leads to ")>-1:
        print(6)
        index1= text.find(" leads to ")
        cause=text[: index1].strip().split(" and ")
        effect=text[index1+10:]
    elif text.find(" will include ")>-1:
        print(7)
        index1= text.find(" will include ")
        cause=text[: index1].strip().split(" and ")
        effect=text[index1+15:]
    elif text.find(" includes ")>-1:
        print(8)
        index1= text.find(" includes ")
        cause=text[: index1].strip().split(" and ")
        effect=text[index1+10:]
    elif text.find('as ')==0:
        print(9)
        index1=text.find('as ')
        index2=text.find(',')
        cause=text[3:index2].strip().split(" and ")
        effect=text[index2 + 1:]  
    elif text.find(", as a result,")>-1:
        print(10)
        index1= text.find(", as a result,")
        cause=text[: index1].strip().split(" and ")
        effect=text[index1+15:]
    elif text.find(" as a result of ")>-1:
        print(11)
        index1= text.find(" as a result of ")
        effect=text[: index1].strip().split(" and ")
        cause=text[index1+16:]
    elif text.find(", consequently ")>-1:
        print(12)
        index1= text.find(", consequently ")
        cause=text[: index1].strip().split(" and ")
        effect=text[index1+15:]
    elif text.find(" so that ")>-1:
        print(13)
        index1= text.find(" so that ")
        cause=text[: index1].strip().split(" and ")
        effect=text[index1+15:]
    elif text.find(", consequently ")>-1:
        print(14)
        index1= text.find(", accordingly ")
        cause=text[: index1].strip().split(" and ")
        effect=text[index1+15:]
    elif text.find(" due to ")>-1:
        print(15)
        index1= text.find(" due to ")
        effect=text[: index1]
        cause=text[index1+15:].strip().split(" and ")
    elif text.find("due to ")>-1:
        print(16)
        index1= text.find(", ")
        effect=text[7: index1]
        cause=text[index1+1:].strip().split(" and ")
    elif text.find(", owning to ")>-1:
        print(17)
        index1= text.find(", owning to ")
        effect=text[: index1]
        cause=text[index1+12:].strip().split(" and ")
    elif text.find("therefore, ")>-1:
        print(18)
        cause= former_sentence
        effect=text[11:]
    
    return cause,effect 
import pandas
import time

q_a = pandas.read_csv("q&A.csv")
qns = list(q_a["Questions"])
ans = list(q_a["Answers"])
msg = " "

name = ["\nI'", "m ", "\"U\"", "\nthe ", "AI ", "Chatbot \n"]


def line(n):
    for i in range(n):
        print("-", end="")
        time.sleep(0.02)


line(15)
for i in range(len(name)):
    print(name[i], end="")
    time.sleep(0.5)
line(15)
print("\n")


flag = True
while flag is True:
    msg = input("Message: ")
    if msg == "quit" or msg == "Quit" or msg == "QUIT":
        flag = False
        break



    l = msg.split()
    ans_set = set()

    for i in range(len(l)):
        for j in range(len(qns)):
            for k in qns[j].split():
                if l[i].lower() == k.lower():
                    ans_set.add(ans[j])

    ans_li = list(ans_set)

    if len(ans_li) == 0:
        if msg == "":
            print("Enter any message")
        elif msg.split("+") or msg.split("-") or msg.split("**") or msg.split("*") or msg.split("/") or msg.split("//") or msg.split("%"):
            try:
                print(eval(msg))
            except ZeroDivisionError:
                print("Number cant divided by 0")
            except NameError:
                print("Oops ! Can't understand your question . Soon u can get the answer !")
                new_qns_file = open("NewQuestions.txt", "a")
                new_qns_file.write(f"{msg}\n")
                new_qns_file.close()
            except SyntaxError:
                print("Oops ! Can't understand your question . Soon u can get the answer !")
                new_qns_file = open("NewQuestions.txt", "a")
                new_qns_file.write(f"{msg}\n")
                new_qns_file.close()
    else:
        for answer in ans_li:
            print(answer)

#GroupName c10_Web016
#leb2Name c10_Web016
# Veerapat Chewprecha 037
# sirawit wirakun 049
# ADITEP PEOMSAP
# 066 Chatuporn Pengpak

#function ที่ใช้ เช็คว่าพวกชื่อ พวก id มันซ่ำหรือมันควรจะเป็นชื่อคนไหม 
def Validation_Name_and_LastName(AllStudentData_Dict,StudentData_List):
    CheckValidation = ['1','2','3','4','5','6','7','8','9','0']
    StudentID = input("ใส่เลขID")
    for i in AllStudentData_Dict:
        if StudentID == i['id']:
            print('รหัสนักศึกษาซ้ำ')
            Select_Option(AllStudentData_Dict,StudentData_List)
    if len(StudentID) == 0:
        print("โปรดใส่ID")
        Select_Option(AllStudentData_Dict,StudentData_List)
    for i in StudentID:
        if i not in CheckValidation:
            print('ใส่ได้แค่ตัวเลข')
            Select_Option(AllStudentData_Dict,StudentData_List) 
    StudentName = input('ใส่ขื้่อ')
    if len(StudentName) == 0:
        print("โปรดใส่ชื่อ")
        Select_Option(AllStudentData_Dict,StudentData_List)
    for i in StudentName:
        if i in CheckValidation:
            print('กรุณาใส่ชื่อให้ถูกต้อง')
            Select_Option(AllStudentData_Dict,StudentData_List)
    StudentLastName = input('ใส่นามสกุล')
    if len(StudentLastName) == 0:
        print("โปรดใส่นามสกุล")
        Select_Option(AllStudentData_Dict,StudentData_List)
    for i in StudentLastName:
        if i in CheckValidation:
            print('กรุณาใส่นามสกุณให้ถูก')
            Select_Option(AllStudentData_Dict,StudentData_List)
    return StudentID,StudentName,StudentLastName

# เก็บข้อมูลนักศึกษาทีกรอก ลงตัวแปรชั่วคราว แล้ว return ออกไปใช้ที่ Select_Option  
def AddStudentToList(StudentID:int , StudentName:str , StudentLastName:str):
    list_id = []
    list_Name = []
    list_LastName = []
    list_id.append(StudentID)
    list_Name.append(StudentName)
    list_LastName.append(StudentLastName)
    return list_id,list_Name,list_LastName

# เก็บข้อมูลนักศึกษาทีกรอก ลงตัวแปรชั่วคราว แล้ว return ออกไปใช้ที่ Select_Option
def AddStudentToDict(StudentID:int,StudentName:str,StudentLastName:str):
    StudentData_To_Dict = {'id':StudentID,"name":StudentName,"lastName":StudentLastName}
    return StudentData_To_Dict


# เป็น function ที่ใช่เพื่อชื่อ นศ ลงตัวแปรชั่วคราว
def AddStudent(StudentID:int,StudentName:str,StudentLastName:str):
    StudentData_To_Dict = AddStudentToDict(StudentID , StudentName , StudentLastName)
    list_id,list_Name,list_LastName = AddStudentToList(StudentID , StudentName , StudentLastName)
    return  StudentData_To_Dict , list_id,list_Name,list_LastName

# แสดงชื่อ นศ 
def ShowStudent(AllStudentData_Dict,StudentData_List):
    print('แสดงชื่อนักศึกษาแบบ Dist')
    for i in AllStudentData_Dict:
        print('ID:',i['id'],"Name:",i['name'],"LastName",i['lastName'])
    print('แสดงแบบ List')
    for k,v in StudentData_List.items():
        for i in range(len(v)):
            print(k,":",v[i] ,end="  |  ")
        print()

#เรียกใช้ function Validation_Name_and_LastName และส่งAllStudentData_Dict,StudentData_List เพื่อไปเช็คว่า ID ที่กำลัง Add ไปใหม่มันตรงกับที่มีอยู่แล้วรึป่าว  เพื่อเช็คให้ถูกว่า ชื่อก็ไ่มควรเป็นตัวเลข อะไรประมาณนั้น
def read_one_student(AllStudentData_Dict,StudentData_List):
    StudentID,StudentName,StudentLastName = Validation_Name_and_LastName(AllStudentData_Dict,StudentData_List)
    return StudentID,StudentName,StudentLastName

#รับ id ที่อยากจะเรียกดูข้อมูล จากนั้น loop ข้อมูลที่เก็บทั้งหมดจาก AllStudentData_Dict 
#โดย ถ้า StudentID ที่กรอกตรงกับ ข้อมูลของ id ที่เรา loop อันไหนเราก็จะดึงข้อมูลนั้นมาแสดง
def Get_Student_Data(AllStudentData_Dict):
    StudentID = input("กรุณาใส่รหัสนักศึกษาที่ต้องการค้นหา: ")
    for i in AllStudentData_Dict:
        if StudentID == i['id'] :
            for k,v in i.items():
                print(f"ข้อมูลที่ค้นพบ: {k,v}")
    print('ไม่พบข้อมูลที่ตรงกับรหัสนักศึกษา')

#function Select_Option เป็น function ที่ให้ user เลือกว่าจะทำอะไรกับหัวข้อที่มีมาให้

#ถ้า User input 1 เข้ามาก็คือเพิ่มข้อมูลนักศึกษา โดยไปเรียกใช้ function read_one_student โดยจะส่งAllStudentData_Dict,StudentData_List เข้าไปด้วยเพื่อเช็คว่า ID ที่ user จะเพิ่มมันมีอยู่แล้วในตัวแปรที่เราเก็บข้อมูลไหม ก่อนเพื่อรับข้อมูลที่User inputเข้ามาโดยจะ return ออกมาเป็น StudentID , StudentName , StudentLastName 
#หลังจากที่ทำในส่วนของ read_one_student เสร็จ จะเรียกใช้ AddStudent โดยส่ง StudentID , StudentName , StudentLastName เข้าไปทำงานเพื่อนำลงไปเก็บไว้ บนตัวแปรชั่วคราว ก่อนนำลงไปเก็บ ลงตัวแปล (AllStudentData_Dict,StudentData_List) ที่เก็บข้อมูลนศ ทั้งหมด
#โดย AddStudent จะ return StudentData_To_Dict,list_id,list_Name,list_LastName 
#ส่วน 4 บรรทัดต่อมาก็จะเอา พวกที่ return ออกมากจากตัวแปรชั่วคราว เอาเข้ามาเก็บบนตัว แปรที่เก็บข้อมูลทั้งหมด

#ถ้า User input 2 เข้ามาก็คือจะเป็นการเรียกดูข้อมูล 
#จะเรียกใช้ function Get_Student_Data โดยส่ง Allstudent_Dict เข้าไป    เพราะว่าเราจะเรียกดูข้อมูลเราต้องส่งตัวแปรท่ี่เก็บข้อมูลไปด้วย เพื่อใช้ID ในการเช็คว่าจะเรียกดู ข้อมูลของคนไหน

#ถ้า User input 3 ก็คือหยุดทำงาน แต่ก่อนหยุดทำงานก็จะให้ show นศ ทั้งหมดก่อนโดยเรียกใช้ function ShowStudent โดยส่ง (AllStudentData_Dict,StudentData_List) เข้าไปทำงานน 

def Select_Option(AllStudentData_Dict,StudentData_List):
    while True:
        Add = input('1)ต้องการเพิ่มข้อมูลนักศึกษา\U0001f600 \n''2)ต้องการเรียกดูข้อมูลนักศึกษา \U0001F606 \n''3)หยุดการทำงาน\U0001F923\n''--->')
        if Add == '1': 
            StudentID , StudentName , StudentLastName = read_one_student(AllStudentData_Dict,StudentData_List)
            StudentData_To_Dict,list_id,list_Name,list_LastName = AddStudent(StudentID , StudentName , StudentLastName)
            AllStudentData_Dict.append(StudentData_To_Dict)
            StudentData_List['id'] += list_id
            StudentData_List['name'] += list_Name
            StudentData_List['LastName'] += list_LastName
        elif Add == '2':
            Get_Student_Data(AllStudentData_Dict)
        elif Add == '3':
            ShowStudent(AllStudentData_Dict,StudentData_List)
            exit()
        else:
            print("โปรดเลือกเลขตามหัวข้อ")

#ในmain() จะเก็บ AllStudentData_Dict ที่เก็บข้อมูลแบบ Array [] แล้วแต่ละ object{}  ก็จะเก็บมาลงใน array AllStudentData_Dict [{"id":"....","name","....","lastname","....."},{},{} ] การเก็บข้อมูลของ AllStudentData_Dict จะเป็นประมาณนี้
#และ StudentData_List จะเป็นในรูปแบบ Object ในแต่ละ value ของแต่ละ Key จะเก็บเป็น Array  StudentData_List = {'id':['001','002'],'name':['a','b'],"LastName":['c','d']}
#พอสร้าง ตัวแปรสองตัวไว้เก็บข้อมูลแล้วก็จะไปเรียกใช้ function Select_Optionและส่ง AllStudentData_Dict , StudentData_List เข้าไปทำงาน

#<------------------เพิ่มเติม---------------------------------------------------------------------------------->
#ที่จริงสร้างตัวแปร แค่AllStudentData_Dict มาเก็บข้อมูลแค่ตัวเด่วก็ได้แต่อันนี้ อาจารย์ อยากให้เก็บข้อมูลทั้งแบบ เป็น object กับ Array 
#<---------------------------------------------------------------------------------------------------------->
def main():
    AllStudentData_Dict = []
    StudentData_List={'id':[],'name':[],"LastName":[]}
    Select_Option(AllStudentData_Dict,StudentData_List)


#เริ่มเรียกใช้งาน function main() 
if __name__ == '__main__':
    main()
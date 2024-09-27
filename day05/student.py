def GPA(student) :
	web = student["units"][0];
	Sys = student["units"][1];
	Jav = student["units"][2];
	
	credits = int(web["credits"]) + int(Sys["credits"]) + int(Jav["credits"]);
	
	res = int(web["credits"]) * int(grade_weight_mapping[web["grade"]]);
	res = res + int(Sys["credits"]) * int(grade_weight_mapping[Sys["grade"]]);
	res = res + int(Jav["credits"]) * int(grade_weight_mapping[Jav["grade"]]);
	
	res = round(res/credits);
	return res;
	
def sortStudentsByName(studs) :
	nom = [];
	res = [];
	for st in studs :
		nom.append(st["name"]);
		
	nom.sort();
	for name in nom :
		for stud in studs :
			if name == stud['name'] :
				res.append(stud);
				
	return res;
	
def sortStudentsByGPA(studs) :
	gpa = [];
	res = [];
	for st in studs :
		gpa.append(st["GPA"]);
		
	gpa.sort();
	for gp in gpa :
		for stud in studs :
			if gp == stud['GPA'] :
				res.append(stud);
				
	return res;

grade_weight_mapping = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "E" : 0};

student = {"name" : "Jb","academic_year" : "2024"}
student.update({"units" : [{"name" : "Web Development", "credits" : 5, "grade" : "D"}, {"name" : "Network and System Administration", "credits" : 20, "grade" : "A"}, {"name" : "Java", "credits" : 10, "grade" : "B"}]});
student.update({"GPA" : GPA(student)});
print(student,"\n");

student2 = {"name" : "Lorine", "academic_year" : "2018"}
student2.update({"units" : [{"name" : "Web Development", "credits" : 5, "grade" : "A"}, {"name" : "Network and System Administration", "credits" : 20, "grade" : "B"}, {"name" : "Java", "credits" : 10, "grade" : "C"}]});
student2.update({"GPA" : GPA(student2)});
print(student2,"\n");

student3 = {"name" : "Eustache", "academic_year" : "2032"}
student3.update({"units" : [{"name" : "Web Development", "credits" : 5, "grade" : "E"}, {"name" : "Network and System Administration", "credits" : 20, "grade" : "E"}, {"name" : "Java", "credits" : 10, "grade" : "E"}]});
student3.update({"GPA" : GPA(student3)});
print(student3,"\n","\n");


myStudents = [student, student2, student3];



myStudents = sortStudentsByGPA(myStudents);
print(myStudents);

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:27:38 2020

@author: Yahan
"""

def read_file(file):
    f = open(file, 'r')
    content = f.readlines()# read file doesn't need close
    return content


#%%
def detect_name(content):
    line1 = content[0].strip()
    words = line1.split(' ')
#    print(words)
    for word in words:
        if not word[0].isupper():
            raise RuntimeError("The name isn\'t with proper capitalization.")
    return line1
#%%
def detect_email(content):
    """Look for a line that has the '@' character.
    Check 1)The last four characters of the email.
    2)There should be no digits or numbers in the email address.
    3)The email string could have leading or trailing whitespace.
    """
    for line in content:
#        print("lineis", line)
        if "@" in line:
            email = line.strip() #the line with @ is the email address
#            print("emailis:", email)
            if ".com" or ".edu" in email[-4:]: #check if it is a correct input
                for i,character in enumerate(email):
                    if character.isdigit():
                        return ""
                    if character == "@":
                        if email[i+1].islower():
                            for j, element in enumerate(email[i+2:]): 
                               if element.isdigit():
                                   return ""
                            return email
            
    return ""

        
#content = ["Yahan Liu", 'liuyahan@seas.upenn.edu', 'liuyahan@seas.upenn.123', 'liuyahan', 'liuyahan@Email.upenn.edu', 
# 'liuyahan@seas.6upenn.edu']
#print(detect_email(content))
#%%
def detect_courses(content):
    """Look for the word "Courses" in the file and then extract the line    
    """      
    for line in content:
        if "Courses" in line:
            #strip the whitespace before and after the line
            line = line.strip()
            
            #get the courses list
            for index, character in enumerate(line[7:]):
                if character.isalpha():
#                    print(character)
#                    print(index)
                    break
            course_list = line[index+7:].split(",")
            for i, course in enumerate(course_list):
                course_list[i] = course.strip()
            
            return course_list
#%%
def detect_projects(content):
    """Look for the word "Projects" in the file
    Each subsequenct line is a project, until you hit a line that looks like '----------'
    """
    projects = []
    
    for index, line in enumerate(content):
        if "Projects" in line:
            break
    for project in content[index+1:]: 
        if "----------" not in project:#when there is -----------, then break the loop
            project = project.strip()
            projects.append(project)
        else:
            break
#    projects = list(filter(lambda project: project!='', projects))
    projects = list(project for project in projects if project!='')
#    print(projects)
    return projects
    
#%%
def surround_block(tag, text):
    """
    This function surrounds the given text with the given HTML tag and returns 
    the string.
    """
    
    block = '<' + tag + '>' + text + '</' + tag + '>' 
    return block

def create_email_link(email_address):
    """This function creates an email link with the given email_address.
    This function should display the email address with an [aT].
    """ 
    
    #If there is @, then we can replace it using [aT]. 
    #If there isn't @, then we don't need to replace it.
    if '@' in email_address:
        email_address_temp = email_address.replace('@', '[aT]')
        link = '<a href=\"mailto:'+email_address+'\">'+email_address_temp+'</a>'
    else:
        link = '<a href=\"mailto:'+email_address+'\">'+email_address+'</a>'
    

    return link

def intro_section(content):
    """Make the entire intro section of the resume
    """
    name = detect_name(content)
    #<h1></h1>block for name
    name_block = surround_block("h1", name)
    email_address = detect_email(content)

    email_link = create_email_link(email_address)

    #<p> block for email address
    email_block = surround_block("p", ("Email:" + email_link))
    #<div> block for intro section
    intro_block = surround_block("div", name_block+email_block)

    return intro_block

def projects_section(content):
    """Use the data about the projects in list.
    """
    projects = detect_projects(content)
    h_block = surround_block("h2", "Projects")
    #for each project, we need a <li> block
    li_block = surround_block("li", projects[0])
    for i in range(len(projects)-1):
        li_block += surround_block("li", projects[i+1])
    #for all the <li> block, we need a <u1> block
    u_block = surround_block("u1", li_block)
    
    #<div> block for projects section
    project_block = surround_block("div", h_block+u_block)

    return project_block

def courses_section(content):
    """Use the data about the courses in list.
    """
    courses = detect_courses(content)
#    print(courses)
    h_block = surround_block("h3", "Courses")
    courses = ",".join(courses)
    span_block = surround_block("span", courses)
    course_block = surround_block("div", h_block+span_block)
#    print(course_block)
    return course_block

def main():
    """
    Open and read resume-temple.html
    read every line of HTML
    Remove the last 2 lines of HTML
    Add all GTML-formatted resume content
    Add the last 2 lines back in
    Write the final HTML to a new file resume.html
    """    
    
    with open("resume_template.html", "r") as f:
        lines = f.readlines()
    
    html = lines[:-2]
    html = "".join(html)

    
    content = read_file("resume.txt")
    intro_block = intro_section(content)
    project_block = projects_section(content)
    course_block = courses_section(content)
    
    #resume_bocdy is the total of those section above.
    resume_body = intro_block+project_block+course_block
    #add the begin and end to the resume_body
    resume = html+'<div id=\"page-wrap\">'+resume_body+"</div></body></html>"
    
    #write the file to txt
    with open("resume.html", "w") as fout:
        fout.writelines(resume)
    fout.close()
             
if __name__ == "__main__":
    main()

            
            
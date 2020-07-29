import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):
    
    def setUp(self):
        self.resume = read_file('resume.txt')
    
    def test_read_fiel(self):
        #test read_file
        with self.assertRaises(FileNotFoundError): read_file("dummy.txt")
        
        self.assertEqual(self.resume[0].strip(), "Yahan Liu")
    
    def test_detect_name(self):
        #test detection when using wrong name.
        with self.assertRaises(RuntimeError): detect_name(["Yahan liu"])
        
        self.assertEqual(detect_name(["Yahan Liu"]), "Yahan Liu")
    
    def test_detect_email(self):
        
        self.assertEqual(detect_email(['liuyahan@seas.upenn.edu']), 'liuyahan@seas.upenn.edu')
        #test detection when using wrong email.
        self.assertEqual(detect_email(['liuyahanaTseas.upenn.edu']), "")
    
    def test_detect_courses(self):
        #test detection when using wrong courses.
        self.assertEqual(detect_courses(['Courses:::::-----     Programming    ,   Machine Learning']), 
                         ["Programming", "Machine Learning"])
        
    def test_detect_projects(self):
        #test detection when using wrong projects.
        self.assertEqual(detect_projects(['Projects', '\t\t\n', '   Project1\n    ',  'Project2', '----------']),
                          ['Project1', 'Project2'])
        
    def test_surround_block(self):

        # test surrounding html
        self.assertEqual(surround_block('h1', 'Eagles'), "<h1>Eagles</h1>")

        # test surrounding html
        self.assertEqual(surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.'),
                                        '<p>Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.</p>')

    def test_create_email_link(self):

        # test created email
        self.assertEqual(
            create_email_link('lbrandon@wharton.upenn.edu'),
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>')

        # test created email
        self.assertEqual(
            create_email_link('lbrandon.at.wharton.upenn.edu'),
            '<a href="mailto:lbrandon.at.wharton.upenn.edu">lbrandon.at.wharton.upenn.edu</a>')
    
    def test_intro_section(self):
        self.assertEqual(intro_section(self.resume),
                         '<div><h1>Yahan Liu</h1><p>Email:<a href="mailto:liuyahan@seas.upenn.edu">liuyahan[aT]seas.upenn.edu</a></p></div>')
    
    def test_projects_section(self):
        self.assertEqual(projects_section(self.resume),
                         '<div><h2>Projects</h2><u1><li>Lenovo AI Lab, Beijing, China - Data science internship, '+ 
                         'transferred the format of audio file. Used Prophet model to predict the express quantity in next three months.</li>'+
                         '<li>Peltast Inc., Chicago, USA - Intern, parsed data from coinmarket.com (using python). '+
                         'Used ARIMA model to predict the cryptocurrency value change in next month.</li></u1></div>')
    
    
    def test_courses_section(self):
        #test if there includes needed block name.
        courses = courses_section(self.resume)
        self.assertTrue('</span>' in courses)
        
if __name__ == '__main__':
    unittest.main()

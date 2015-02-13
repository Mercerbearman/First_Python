'''
Created on Feb 9, 2015

@author: Fox
'''

if __name__ == '__main__':
    #import entire class for sqLite.
    #from sqLite import sqLite_Test
    from First.sqLite import *
    sq = sqLite_Test()
    
    #Grab all functions in sqLite_Test
    allSqLiteFuncts = dir(sqLite_Test)
    print('Class {0} - Interface {1}'.format(sqLite_Test, allSqLiteFuncts))
    
    #Here we use the First. to get to the sub directory
    #Sub directory must have "__init__.py" file in it for this to work.
    from First.OpenCV import OpenCV_Test
    cv = OpenCV_Test()
    
    #Grab all functions in OpenCV_Test
    allOpenCV_TestFuncts = dir(OpenCV_Test)
    print('Class {0} - Interface {1}'.format(OpenCV_Test, allOpenCV_TestFuncts))
    
    sq.sqLite_Work()
    pass

'''
Created on Feb 9, 2015

@author: Fox
'''

class OpenCV_Test(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def TempFunct(self):
        print('In OpenCV_Test::TempFunct')
        
    def GetImageText(self):
    #def GetImageText(self''',cv2.Mat'''):
        
        import cv2
        
        #http://stackoverflow.com/a/23672571
        
        large = cv2.imread('First\Receipts\Pump-1.JPG',cv2.IMREAD_COLOR)
        #Downsample original image.
        #C++ format in ''' ''' 
        '''pyrDown(large, rgb); '''
        rgb = cv2.pyrDown(large)
        
        ''' cvtColor(rgb, small, CV_BGR2GRAY); '''
        small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
        
        #Morphological Gradient
        #WTF...
        ''' Mat morphKernel = getStructuringElement(MORPH_ELLIPSE, Size(3, 3)); '''
        morphKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
        ''' morphologyEx(small, grad, MORPH_GRADIENT, morphKernel); '''
        grad = cv2.morphologyEx(small,cv2.MORPH_GRADIENT,morphKernel, iterations = 1)
        
        #binarize...
        '''threshold(grad, bw, 0.0, 255.0, THRESH_BINARY | THRESH_OTSU); '''
        bw = cv2.threshold(grad,0.0,255.0,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        #Connect Horizontally oriented regions
        '''morphKernel = getStructuringElement(MORPH_RECT, Size(9, 1));'''
        morphKernel = cv2.getStructuringElement(cv2.MORPH_RECT,(9,1))
        '''morphologyEx(bw, connected, MORPH_CLOSE, morphKernel); '''
        connected = cv2.morphologyEx(bw,cv2.MORPH_CLOSE,morphKernel, iterations = 1)
        
        #Find Contours
        ''' findContours(connected, contours, hierarchy, CV_RETR_CCOMP, CV_CHAIN_APPROX_SIMPLE, Point(0, 0)); '''
        contours, hierarchy = cv2.findContours(connected, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        #This is a potential solution for the offset of Point(0,0) I think.
        #contours, hierarchy = cv2.findContours(connected, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE, (0,0))
        
        '''
        #Filter Contours
        for(int idx = 0; idx >= 0; idx = hierarchy[idx][0])
        {
            Rect rect = boundingRect(contours[idx]);
            Mat maskROI(mask, rect);
            maskROI = Scalar(0, 0, 0);
            // fill the contour
            drawContours(mask, contours, idx, Scalar(255, 255, 255), CV_FILLED);
            // ratio of non-zero pixels in the filled region
            double r = (double)countNonZero(maskROI)/(rect.width*rect.height);
    
            if (r > .45 /* assume at least 45% of the area is filled if it contains text */
                && 
                (rect.height > 8 && rect.width > 8) /* constraints on region size */
                /* these two conditions alone are not very robust. better to use something 
                like the number of significant peaks in a horizontal projection as a third condition */
                )
            {
                rectangle(rgb, rect, Scalar(0, 255, 0), 2);
            }
        }
        imwrite(OUTPUT_FOLDER_PATH + string("rgb.jpg"), rgb);
    
        return 0;
        '''
        

    def Initial(self):
        import cv2
        print (cv2.__version__)
        
        #Grab a path to the image.
        image = cv2.imread('First\Receipts\Pump-1.JPG',cv2.IMREAD_COLOR)
        #Test the path with a print.  If we get something other than "None" we have loaded the image.
        print (image)
        
        
        #Now to try to display said image.
        #Display one.
        cv2.imshow('Pumping', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        #Display two.
        #This one scales it to a normal windows size.
        cv2.namedWindow("Das Pump",cv2.WINDOW_NORMAL)
        cv2.imshow("Das Pump", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        #OpenCV_Test.GetImageText(OpenCV_Test)

        
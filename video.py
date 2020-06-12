import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    
    # Blur using 3 * 3 kernel. 
    gray_blurred = cv2.blur(gray, (3, 3)) 
    
    # Apply Hough transform(there's a good document that explains that) on the blurred image. 
    detected_circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,param2 = 30, minRadius = 30, maxRadius = 80) 
    def distance(x1,y1,x2,y2):
        dist= ((((x1-x2)**2)+((y1-y2)**2))**0.5)/avunit
        return dist

    sum=0
    c=0
    xc=[]
    yc=[]
    # Draw circles that are detected. 
    if detected_circles is not None: 
    
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
    
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            c=c+1
            # Draw the circumference of the circle. 
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2) 
    
            # Draw a small circle (of radius 1) to show the center. 
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3) 
            cv2.imshow("Detected Circle", frame) 
            sum=r+sum
            xc.append(a)
            yc.append(b)
        
    avunit=(sum/(c))
    for i in range(c-1):
        dist=distance(int(xc[i]),int(yc[i]),int(xc[i+1]),int(yc[i+1]))
        print(dist)
        start_point=(xc[i],yc[i])
        color=(0,0,255)
        end_point=(xc[i+1],yc[i+1])
        thickness=2
        frame=cv2.line( frame, start_point , end_point, color, thickness)
        cv2.imshow("Detected Circle", frame)
        # cv2.waitKey(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame=cv2.putText(frame,'Length='+str(dist),((int(xc[i])+int(xc[i+1]))//2,(int(yc[i])+int(yc[i+1]))//2), font, 0.5,(0,0,0),2,cv2.LINE_AA)
        cv2.imshow("Detected Circle", frame)
    dist1=distance(int(xc[0]),int(yc[0]),int(xc[c-1]),int(yc[c-1]))
    print(dist1)
    start_point=(xc[0],yc[0])
    color=(0,0,255)
    end_point=(xc[c-1],yc[c-1])
    thickness=2
    frame=cv2.line( frame, start_point , end_point, color, thickness)
    cv2.imshow("Detected Circle", frame)
    # cv2.waitKey(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    frame=cv2.putText(frame,'Length='+str(dist1),((int(xc[0])+int(xc[c-2]))//2,(int(yc[0])+int(yc[c-1]))//2), font, 0.5,(0,0,0),2,cv2.LINE_AA)
    cv2.imshow("Detected Circle", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
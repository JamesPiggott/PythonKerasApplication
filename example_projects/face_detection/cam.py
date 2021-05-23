import cv2
from retinaface import RetinaFace

cap = cv2.VideoCapture(0)



while(cap.isOpened()):

    _, frame = cap.read()
    if frame is None:
        print("no cam input")

    resp = RetinaFace.detect_faces(frame)

    # draw results
    #for prior_index in range(len(faces)):
    #    draw_bbox_landm(frame, faces[prior_index], frame_height,
    #                    frame_width)

    # calculate fps
    #fps_str = "FPS: %.2f" % (1 / (time.time() - start_time))
    #start_time = time.time()
    #cv2.putText(frame, fps_str, (25, 25),
    #            cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 255, 0), 2)

    # show frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        exit()


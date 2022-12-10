from flask import  Blueprint,request
import  cv2
count_bp=Blueprint('count',__name__,url_prefix='/user')
@count_bp.route('/count',methods=["POST","GET"])
def count_people():
    if request.method=='POST':
        upload_file = request.files['file']
        filename = upload_file.filename
        if filename != '':
            upload_file.save('static/images/count/' + filename)
        config_file = 'static/config/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt';
        frozen_model = 'static/ssd_mobilenet/frozen_inference_graph.pb'
        model = cv2.dnn_DetectionModel(frozen_model, config_file)
        classLabels = []
        file_name = 'static/Labels.txt'
        with open(file_name, 'rt') as fpt:
            classLabels = fpt.read().rstrip('\n').split('\n')
        model.setInputSize(320, 320)
        model.setInputScale(1.0 / 127.5)
        model.setInputMean(127.5)
        model.setInputSwapRB(True)

        img = cv2.imread('static/images/count/' + filename)

        ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)
        count = 0
        font_scale = 1
        font = cv2.FONT_HERSHEY_PLAIN
        for ClassInd, conf, boxes in zip(ClassIndex.flatten(), confidence.flatten(), bbox):
            if classLabels[ClassInd - 1] == 'person':
                count += 1
                cv2.rectangle(img, boxes, (255, 0, 0), 1)
                cv2.putText(img, classLabels[ClassInd - 1], (boxes[0] + 10, boxes[1] + 40), font, fontScale=font_scale,
                            color=(0, 255, 0), thickness=3)
        cv2.imwrite('static/images/count/'+filename,img)
        return {
            'count': str(count),
            'url':'http://127.0.0.1:5000/static/images/count/'+filename
        }


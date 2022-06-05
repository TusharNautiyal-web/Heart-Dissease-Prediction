from pydantic import BaseModel

class hd(BaseModel):
    sex : int
    cp : int
    trestbps : int
    age : int
    oldpeak : float
    exang : int
    fbs : int
    restecg : int
    thalach : int
    slope : int
    thal : int
    chol : int
    ca : int


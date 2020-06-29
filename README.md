## SST-FeatureEngineerings

## SST(Singular Spectrum Transformation)

```
from sst import SingularSpectrumTransformation
score = SingularSpectrumTransformation(win_length=30, n_components=2, use_lanczos=True).score_offline(x)
plot_data_and_score(x,score)
 
d1 = pd.read_csv('test_data.csv')
d1 = d1.reshape(2048)
score = SingularSpectrumTransformation(win_length=30, n_components=2, use_lanczos=True).score_offline(d1)
plot_data_and_score(d1,score)

```
<img src="https://user-images.githubusercontent.com/48679574/85997882-0fdef080-ba45-11ea-8f7c-4aa0fc17c893.png" width="700px">



## DTW(Dynamic Time Warping)

```
from dtaidistance.dtw1 import calc_dtw, plot_path
import pandas as pd

def pdTo1dim(df_):
    numpy_ = df_.values
    H, W = np.shape(numpy_)
    return numpy_.reshape(H)
def plot_dtw1(d1, d2):
    # DTWの仕組み => 2つの時系列の縦軸の距離を計算
    m = calc_dtw(d1, d2)
    A=d1
    B=d2

    plot_path(m, A, B)
    print("A-B distance: ", calc_dtw(A, B)[-1][-1][0])
    
d1 = pd.read_csv('test_data1.csv', index_col=0)
d2 = pd.read_csv('test_data2.csv', index_col=0)
d1 = pdTo1dim(d1)
d2 = pdTo1dim(d2)
# dtw
plot_dtw1(d1, d2)
```
<img src="https://user-images.githubusercontent.com/48679574/85997898-140b0e00-ba45-11ea-9a14-1de2acbc15ff.png" width="700px">


"""
    Copyright 2019 Samsung SDS
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import unittest
import numpy as np
from sklearn.model_selection import train_test_split
from brightics.common.datasets import load_iris
from brightics.function.regression import knn_regression
import HtmlTestRunner
import os


class TestKNNRegression(unittest.TestCase):

    def test_default(self):
        df_iris = load_iris()
        df_train, df_test = train_test_split(df_iris, random_state=12345)
        df_res = knn_regression(train_table=df_train, test_table=df_test,
                                feature_cols=['sepal_length', 'sepal_width'], label_col='petal_length',
                                k=5, algorithm='auto', leaf_size=30, p=2)['out_table']
                                   
        np.testing.assert_array_almost_equal([4.0, 1.3800000000000001, 5.22, 1.52, 1.6800000000000002],
                                             df_res['prediction'].values[:5], 10, 'incorrect prediction')

    def test_optional(self):
        df_iris = load_iris()
        df_train, df_test = train_test_split(df_iris, random_state=12345)
        df_res = knn_regression(train_table=df_train, test_table=df_test,
                                    feature_cols=['sepal_length', 'sepal_width', 'petal_length'], label_col='petal_width',
                                    k=3, algorithm='auto', leaf_size=10, p=2)['out_table']
        
        np.testing.assert_array_almost_equal([1.1333333333333335, 0.2333333333333333, 1.5666666666666667, 0.2333333333333333, 0.2333333333333333],
                                             df_res['prediction'].values[:5], 10, 'incorrect prediction')


if __name__ == '__main__':
    filepath = os.path.dirname(os.path.abspath(__file__))
    reportFoler = filepath + "/../../../../../../../reports"
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, output=reportFoler))

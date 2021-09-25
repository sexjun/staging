#include<iostream>
#include<stdio.h>
#include<opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {
    Mat image_in = imread("1.png");
    namedWindow("show_imput_image", 1);
    imshow("show_input_image", image_in);
    waitKey(0);
    return 0;
}



var data = [];


var m = 0;
var b = 0;

var learning_rate = 0.01;

function setup()
{
  createCanvas(400,400);
  background(239, 131, 16);
}

function mousePressed()
{
     var x = map(mouseX,0,width,0,1);
     var y = map(mouseY,0,height,1,0);

     var point = createVector(x,y);
     data.push(point);
     //linearRegression();
}


function linearRegression()
{
     var xsum = 0;
     var ysum = 0;
     for(var i = 0;i<data.length ; i++)
     {
          xsum += data[i].x;
          ysum += data[i].y;
     }

     var xavg = xsum / data.length;
     var yavg = ysum / data.length;


     var numerator = 0;
     var den = 0;
     for(var i = 0;i<data.length ; i++)
     {
          numerator += (data[i].x - xavg) * (data[i].y - yavg);
          den +=  (data[i].x - xavg) * (data[i].x - xavg) ;
     }
     if(den == 0)
     {
          den = 0.01;
     }
     m = numerator / den;
     b = yavg - m * xavg;

}


function gradientDescent()
{
     var deltaM = 0;
     var deltaB = 0;
     for(var i = 0; i < data.length ; i++)
     {
          deltaM += m*data[i].x + b - data[i].y;
          deltaB += (m*data[i].x + b - data[i].y) * data[i].x;

     }

     deltaM = (deltaM / data.length)*learning_rate;
     deltaB = (deltaB / data.length)*learning_rate;

     m = m -deltaM;
     b = b - deltaB;

}

function drawLine()
{
     var x1 = 0;
     var y1 = m * x1 + b;
     var x2 = 1;
     var y2 = m * x2 + b;


     x1  = map(x1 , 0 , 1 , 0 , width);
     x2  = map(x2 , 0 , 1 , 0 , width);
     y1  = map(y1 , 0 , 1 , height , 0);
     y2  = map(y2 , 0 , 1 , height , 0);

     stroke(209, 33, 194);
     line(x1,y1,x2,y2);

}

function draw()
{
     background(239, 131, 16);
     for(var i = 0; i < data.length ; i++)
     {
          var x = map(data[i].x,0,1,0,width);
          var y = map(data[i].y,1,0,0,height);
          fill(40);
          stroke(150);
          ellipse(x,y,8,8);
     }

     if(data.length>1)
     {
          gradientDescent();
          drawLine();
          console.log(m,b);
     }

}

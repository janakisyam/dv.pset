function setup()
{
  createCanvas(800,800);
  strokeWeight(2);
  noFill();
}
var w=100,h=100,x=0,x1,y;
function draw()
{

  translate(200,200);


    x1 = 100*cos(x*PI/1600)+100;
    y = 50*sin(x*PI/1600)+100;
    clear();
    //ellipse(w,h,200,100);
    x = x+5;
    ellipse(x1,y,30,30);
    ellipse(w,h,50,50);


  //x1 = 10*cos(x*PI/16)+50;
  //y = 10*sin(x*PI/16)+50;

  //ellipse(x1,y,100,100);
}

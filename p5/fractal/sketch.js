var angle;

var slider;
function setup()
{
    createCanvas(400, 400);
    slider = createSlider(0, TWO_PI, PI/4, 0.01);
}   

function draw()
{
    background(51);
    angle = slider.value();
       
    translate(200, height);
    Branch(110);
}

function Branch(len)
{
    stroke(len * 7);
    line(0, 0, 0, -len);
    translate(0, -len);
        

    if(len > 2){
        push();
        rotate(angle);
        Branch(len*0.67);
        pop();
        push();
        rotate(-angle);
        Branch(len*0.67);
        pop();
    }
    
}
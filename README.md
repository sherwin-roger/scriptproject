# Mathematical Calculations using JavaScript
## AIM:
To design a website to calculate the area of a circle and volume of a cylinder using JavaScript.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Write JavaScript to perform calculations.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 6:
Publish the website in the given URL.


## PROGRAM:
```
<script>
    document.getElementById('submit').onclick = volume;

    function volume() {
  
        var r = document.getElementById('r').value;
        r = Number(r);
        console.log(r)
  
        var h = document.getElementById('h').value;
        h = Number(h);
  
        var answer=Math.PI*r*r*h;
        console.log(answer)

        document.getElementById('volume').innerHTML = parseFloat(answer);
  
}
</script>
```
## OUTPUT:
![output](./static/img/output.png)

## RESULT:
Thus a website is designed for the volume of cylinder and area of triangle is done and it is hosted in the URL http://sherwin.student.saveetha.in:8000/volumeofcylinder. HTML code is validated.
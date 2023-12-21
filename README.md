# TouchScript
"TouchScript" is an innovative project aimed at enhancing accessibility and inclusivity in experiencing textual content and visual imagery. 

TouchScript is a cutting-edge project designed to improve inclusivity and accessibility when interacting with text and images. This innovative tool fosters a new way of interacting with information by smoothly converting text into Braille patterns and analyzing images to create tactile representations. The control system simulated here is rendered by using a display containing 20 columns and 10 rows of tactile raisable dots. The dots are raised to simulate the braille texts or the outlines of the images for identification.

Its main feature is the ability of TouchScript to convert text to Braille. Any text can be entered by users, and the program converts it into matching Braille patterns. The Braille patterns have been referred from [PharmaBraille]([url](https://www.pharmabraille.com/braille-codes/unified-english-braille-ueb-code/)). This website contains braille used in various parts of the world. The Brailled chosen here is the Unified English Braille (UEB) Code. The authorities of Australia, Canada, New Zealand, Nigeria, South Africa, the UK, Ireland, and the US have adopted UEB as their primary braille code. All the letters and numbers along with certain punctuations have been addressed in the simulation design. This tool also creates opportunities for people with visual impairments to interact and comprehend written information more deeply by providing tactile access to textual content.

The tool's functionality is also expanded to include images. Images uploaded by users are processed by TouchScript to produce tactile representations appropriate for touch exploration. The user can input any image(black and white) into the GUI which processes the image using various image processing techniques to alter, resize, and raise the dots according to the outlines of the image and lower the dots around the white parts. In addition to assisting the blind, this feature allows any user who wants to explore visual content via touch-based interfaces to have a unique sensory experience. 

Demystifying access to knowledge and experiences is central to the project's philosophy. Through an immersive approach to written content and visual imagery, it seeks to remove barriers for people with visual impairments. By giving conventional text and images a tactile quality, it also improves the experience for all users and encourages a closer relationship with the content than is possible with just visual perception.

TouchScript exemplifies the use of technology to promote social inclusion and a variety of ways to engage and experience content. Making information more interactive and accessible for a larger audience, its features promote inclusivity.

PharmaBraille - https://www.pharmabraille.com/braille-codes/unified-english-braille-ueb-code/

# Results
TouchScript tool has been deployed for the user using the Tkinter library in Python. This is a very simple GUI form and was created to avoid further complications in the code to just serve the purpose of a prototype.

 **Steps to Run**
1. Save the TorchScript file on a folder and run the Python file on the terminal and a box similar to what's shown below will be seen 

<img width="366" alt="Screenshot 2023-12-21 at 11 11 24 PM" src="https://github.com/pallavisharma03/TouchScript/assets/137420837/0c6fd534-0cf9-49e5-b4b0-01af2dabe9a3">

2. You can now use the text box displayed to convert the text into braille codes displayed on a 10X20 tactile board which shows the output on the terminal as shown below using the "Process Text" button.

<img width="366" alt="Screenshot 2023-12-21 at 11 11 32 PM" src="https://github.com/pallavisharma03/TouchScript/assets/137420837/fb40ad0e-ab33-4894-81de-2213d2e43389">
<img width="366" alt="Screenshot 2023-12-21 at 11 12 29 PM" 
  src="https://github.com/pallavisharma03/TouchScript/assets/137420837/82b39c00-19ba-4d4c-8cc3-5c28df376323">
  
  You can display numeric values as well which is indicated by a prefix of "#" which acts as a number identifier   and is also displayed in braille before the number.

<img width="366" alt="Screenshot 2023-12-21 at 11 12 19 PM" src="https://github.com/pallavisharma03/TouchScript/assets/137420837/07aae2b4-7bf0-4092-89fc-fda42cb04ebd">

<img width="366" alt="Screenshot 2023-12-21 at 11 11 50 PM" src="https://github.com/pallavisharma03/TouchScript/assets/137420837/71f2c068-c5ad-482b-8fa1-666471ba1702">

  Some basic punctuations are included in the code too!

  
<img width="366" alt="Screenshot 2023-12-21 at 11 12 47 PM" src="https://github.com/pallavisharma03/TouchScript/assets/137420837/048e4060-8758-4f33-b3e3-fd3b3207c636">
<img width="366" alt="Screenshot 2023-12-21 at 11 12 58 PM" src="https://github.com/pallavisharma03/TouchScript/assets/137420837/1943ff74-4322-4d60-b5af-c41cb6a8ee87">

3. You can input images to be processed as well. When you click on the "Process Image button", a window similar to what's shown below pops up.

<img width="366" alt="Screenshot 2023-12-21 at 11 13 37 PM" src="https://github.com/pallavisharma03/TouchScript/assets/137420837/f02591b0-3144-4b9d-a8ca-c2a90f2c9191">

  For inputs, you can use images similar to the one shown below.

<img width="366" alt="Screenshot 2023-12-20 at 10 20 13 PM" src="https://github.com/pallavisharma03/TouchScript/assets/137420837/5b31c3f2-ba20-46f9-951b-8c0915a80329">
  
  Your outputs will be hence like:

<img width="366" alt="Screenshot 2023-12-21 at 11 14 04 PM" src="https://github.com/pallavisharma03/TouchScript/assets/137420837/1b1f10a4-688d-4406-abec-af18cb1f1257">


4. You can use the "Refresh Terminal" button to clear out past outputs in the terminal




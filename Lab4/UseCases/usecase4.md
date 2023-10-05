**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Drag And Draw Over The Canvas

**Primary Actor**: user

**Goal in Context**: to change the color of pixels on the canvas by pressing the left mouse button and dragging, creating a drawing or pattern on the canvas.

**Preconditions**: The graphics program must be running and in a responsive state. The user must have previously selected a color.

**Trigger**: The user presses and holds the left mouse button and moves the mouse to draw on the canvas.

**Scenario**: 1. The user presses and holds the left mouse button (left-click) without releasing it. 2. As the user moves the mouse while holding the left button, the application detects the mouse movement and continuously updates the pixel color beneath the cursor with the selected drawing color. 3. The user can drag the mouse to create lines, shapes, or patterns on the canvas with the selected color. 4. The user can release the left mouse button to stop drawing or continue by pressing and holding the button again. 5. If the user wishes to change the drawing color while drawing, they can do so by selecting a different color from the color palette or interface controls.

**Exceptions**: If the user tries to draw without selecting a drawing color, the application should provide feedback, such as an error message or a reminder to select a color first.

**Priority**: high

**When available**: first release

**Channel to actor**: The primary actor interacts with the system through the mouse input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: N/A

<hr>

(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)

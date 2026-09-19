# The n8n Screen

## 🎯 Goal

- Find your way around the n8n screen
- Build and run a small workflow

## 🧠 In Simple Words

You build a workflow by adding boxes on a big empty screen.
Then you join the boxes in order.

## 🖼️ The Canvas

The canvas is the big empty area in the middle.
Your workflow lives here.

## ➕ Add a Node

Click the **+** button.
Type the name of the node you want, then click it.

## 🔗 Connect Nodes

Every node has a small dot on its right side.
Drag from that dot to the next node.

```text
Node 1  ●———→  Node 2
```

## 🔍 Inside a Node

Double-click a node to open it. It has three parts:

```text
INPUT     |    SETTINGS    |    OUTPUT
what came      what this       what goes
    in         node does           out
```

Left is what came in. Middle is what you change. Right is the result.

## ▶️ Test Workflow

The **Test workflow** button is at the bottom.
It runs the workflow one time so you can see the output.

## 💪 Try It

Add a **Manual Trigger**, then add an **Edit Fields** node.
Connect them and click **Test workflow**.
Open the second node and look at the OUTPUT side.

## ✅ Remember

- Canvas = where you build
- **+** = add a node
- Dot to node = connect
- INPUT left, SETTINGS middle, OUTPUT right

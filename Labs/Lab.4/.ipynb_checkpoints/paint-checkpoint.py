{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b650f231",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Canvas:\n",
    "    def __init__(self, width, height):\n",
    "        self.width = width\n",
    "        self.height = height\n",
    "        self.data = [[' '] * width for i in range(height)]\n",
    "\n",
    "    def set_pixel(self, row, col, char='*'):\n",
    "        self.data[row][col] = char\n",
    "\n",
    "    def clear_canvas(self):\n",
    "        self.data = [[' '] * self.width for i in range(self.height)]\n",
    "\n",
    "    def v_line(self, x, y, w, **kargs):\n",
    "        for i in range(x, x+w):\n",
    "            self.set_pixel(i, y, **kargs)\n",
    "\n",
    "    def h_line(self, x, y, h, **kargs):\n",
    "        for i in range(y, y+h):\n",
    "            self.set_pixel(x, i, **kargs)\n",
    "\n",
    "    def line(self, x1, y1, x2, y2, **kargs):\n",
    "        slope = (y2 - y1) / (x2 - x1)\n",
    "        for y in range(y1, y2):\n",
    "            x = int(slope * y)\n",
    "            self.set_pixel(x, y, **kargs)\n",
    "\n",
    "    def display(self):\n",
    "        print(\"\\n\".join([\"\".join(row) for row in self.data]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "19144098",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Shape:\n",
    "    def paint(self, canvas):\n",
    "        raise NotImplementedError(\"paint() not implemented\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e49bd90f",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Rectangle(Shape):\n",
    "    def __init__(self, length, width, x, y, char='*'):\n",
    "        self.length = length\n",
    "        self.width = width\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.char = char\n",
    "\n",
    "    def boundary_points(self):\n",
    "        points = []\n",
    "        n = 4\n",
    "        for i in range(n):\n",
    "            points.append((self.x + i*self.length/n, self.y))\n",
    "        for i in range(n):\n",
    "            points.append((self.x + self.length, self.y + i*self.width/n))\n",
    "        for i in range(n):\n",
    "            points.append((self.x + self.length - i*self.length/n, self.y + self.width))\n",
    "        for i in range(n):\n",
    "            points.append((self.x, self.y + self.width - i*self.width/n))\n",
    "        return points\n",
    "\n",
    "    def paint(self, canvas):\n",
    "        for (x, y) in self.boundary_points():\n",
    "            canvas.set_pixel(int(y), int(x), char=self.char)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "4562f1cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "\n",
    "class Circle(Shape):\n",
    "    def __init__(self, radius, x, y, char='o'):\n",
    "        self.radius = radius\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.char = char\n",
    "\n",
    "    def boundary_points(self):\n",
    "        points = []\n",
    "        n = 16\n",
    "        for i in range(n):\n",
    "            theta = 2 * math.pi * i / n\n",
    "            points.append((\n",
    "                self.x + self.radius * math.cos(theta),\n",
    "                self.y + self.radius * math.sin(theta)\n",
    "            ))\n",
    "        return points\n",
    "\n",
    "    def paint(self, canvas):\n",
    "        for (x, y) in self.boundary_points():\n",
    "            canvas.set_pixel(int(y), int(x), char=self.char)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "66567f52",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Triangle(Shape):\n",
    "    def __init__(self, base, height, x, y, char='^'):\n",
    "        self.base = base\n",
    "        self.height = height\n",
    "        self.x = x\n",
    "        self.y = y\n",
    "        self.char = char\n",
    "\n",
    "    def boundary_points(self):\n",
    "        points = []\n",
    "        n = 5\n",
    "        for i in range(n):\n",
    "            points.append((self.x + i*self.base/n, self.y))\n",
    "        for i in range(n):\n",
    "            points.append((self.x, self.y + i*self.height/n))\n",
    "        for i in range(n):\n",
    "            t = i/n\n",
    "            points.append((self.x + t*self.base, self.y + t*self.height))\n",
    "        return points\n",
    "\n",
    "    def paint(self, canvas):\n",
    "        for (x, y) in self.boundary_points():\n",
    "            canvas.set_pixel(int(y), int(x), char=self.char)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3c27154e",
   "metadata": {},
   "outputs": [],
   "source": [
    "class CompoundShape(Shape):\n",
    "    def __init__(self, shapes):\n",
    "        self.shapes = shapes\n",
    "\n",
    "    def paint(self, canvas):\n",
    "        for shape in self.shapes:\n",
    "            shape.paint(canvas)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "728dcd99",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

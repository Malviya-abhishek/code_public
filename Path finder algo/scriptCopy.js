const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')
let start, end
canvas.height = 800
canvas.width = 1000
canvas.style = "border: 1px solid black"
canvas.style = "background-color: rgba(123, 123, 213, .5)"

let value

function input() {
    value = document.getElementById("dropDown").value
    if (value == 0)
        value = undefined
    console.log(value)
}



const cellSize = 20
const numOfRow = canvas.height / cellSize
const numOfCol = canvas.width / cellSize
let eventListenerStatus = true
let openList = []
let rows = [0, -1, 0, 1]
let cols = [1, 0, -1, 0]

let fMultiple = 1
let gMultiple = 1
let hMultiple = 1

var rect = canvas.getBoundingClientRect();


const offSetHeight = rect.top
const offSetWidth = rect.left

function hurestic(cell) {
    return (cell.i - end[0]) ** 2 + (cell.j - end[1]) ** 2
}

class Cell {
    constructor(i, j, colour, distance, status) {
        this.i = i
        this.j = j
        this.colour = colour
        this.f = Infinity
        this.g = distance
        this.h = Infinity

        ctx.beginPath()
        ctx.arc(this.j * cellSize + cellSize / 2, this.i * cellSize + cellSize / 2,cellSize/2,0,Math.PI*2)
        ctx.stroke()


        this.status = status
        this.neighbours = []
        this.parent = null
    }

    draw() {
        ctx.fillStyle = this.colour
        ctx.beginPath()
        ctx.arc(this.j * cellSize + cellSize / 2, this.i * cellSize + cellSize / 2, cellSize / 2, 0, Math.PI * 2)
        ctx.fill()
    }

    addNeighbours(mat_given) {
        for (let i = 0; i < cols.length; ++i) {
            let itemp = this.i + cols[i]
            let jtemp = this.j + rows[i]
            if (itemp >= 0 && itemp < numOfRow && jtemp >= 0 && jtemp < numOfCol && mat_given[itemp][jtemp].status)
                this.neighbours.push(mat_given[itemp][jtemp])
        }
    }

}


let mat = new Array(numOfRow)

for (let i = 0; i < numOfRow; ++i)
    mat[i] = new Array(numOfCol)


for (let i = 0; i < mat.length; i++)
    for (let j = 0; j < mat[i].length; ++j)
        mat[i][j] = new Cell(i, j, "white", Infinity, true)


window.addEventListener('click', mouseClick);
window.addEventListener('mousemove', mousePress);
window.addEventListener('keydown', keyPress);

function keyPress(event) {

    if (event.key == "Enter" && value) {
        eventListenerStatus = false
        window.removeEventListener('click', mouseClick);
        window.removeEventListener('mousemove', mousePress);
        window.removeEventListener('keydown', keyPress);


        if (value == 1) {
            hMultiple = 0
            gMultiple = 1
            findPath()
        }
        else if (value == 2) {
            hMultiple = 1
            gMultiple = 1
            findPath()
        }
        else if (value == 3) {
            gMultiple = 0
            hMultiple = 1
            findPath()
        }
        else if (value == 4) {
            hMultiple = 0
            gMultiple = 1
            biDirectional()
        }

        console.log(hMultiple, gMultiple)
    }
    else if (event.key == "r") {
        console.log("ashfoah")
        randomFill()
    }
}

function mouseClick(event) {
    let i = Math.floor((event.clientY - offSetHeight) / cellSize)
    let j = Math.floor((event.clientX - offSetWidth) / cellSize)

    if (i < 0 || i >= numOfRow || j < 0 || j >= numOfCol)
        return;

    if (!start && mat[i][j].status) {
        start = [i, j]
        mat[i][j].colour = "green"
        mat[i][j].parent = mat[i][j]
        mat[i][j].g = 0
        mat[i][j].draw()
        openList.push(mat[i][j])
    }
    else if (!end && (start[0] != i || start[1] != j) && mat[i][j].status) {
        end = [i, j]
        mat[i][j].colour = "#00008B"
        mat[i][j].draw()
    }
}

function mousePress(event) {
    // console.log(event)
    if (start == undefined || end == undefined)
        return;

    let i = Math.floor((event.clientY - offSetHeight) / cellSize)
    let j = Math.floor((event.clientX - offSetWidth) / cellSize)


    if (help()) {
        mat[i][j].colour = "black"
        mat[i][j].status = false
        mat[i][j].draw()
    }

    function help() {
        let flag = event.buttons == 1 && i >= 0 && i < numOfRow && j >= 0 && j < numOfCol;
        if (!flag) return flag;
        flag = flag && (start && end)
        if (!flag) return flag;
        flag = flag && ((start[0] != i || start[1] != j) && (end[0] != i || end[1] != j) && mat[i][j].status)
        return flag;
    }
}


function findPath() {

    for (let i = 0; i < numOfRow; ++i)
        for (let j = 0; j < numOfCol; ++j)
            if (mat[i][j].status) {
                mat[i][j].addNeighbours(mat);
                mat[i][j].h = hurestic(mat[i][j])
            }
    openList[0].f = openList[0].g * gMultiple + openList[0].h * hMultiple

    let currentCell = null
    let timeId

    timeId = setInterval(() => {
        if (openList[0] && mat[end[0]][end[1]].status) {
            console.log("hello");
            let index = 0

            for (let i in openList)
                if (openList[index].f > openList[i].f)
                    index = i

            let tempCell = openList[index]
            let neighbours = tempCell.neighbours

            openList.splice(index, 1)
            tempCell.status = false

            if (tempCell.colour != "green") {
                tempCell.colour = "#ade6d8"
                tempCell.draw()
            }

            for (let i in neighbours) {
                if (neighbours[i].status)
                    if (neighbours[i].g > tempCell.g + 1) {
                        neighbours[i].g = tempCell.g + 1
                        neighbours[i].f = neighbours[i].g * gMultiple + neighbours[i].h * hMultiple
                        neighbours[i].parent = tempCell
                        let neighbourIndex = openList.findIndex(item => (item.i == neighbours[i].i && item.j == neighbours[i].j))
                        if (neighbourIndex == -1) {
                            if (neighbours[i].colour != "#00008B") {
                                neighbours[i].colour = "#add8e6"
                                neighbours[i].draw()
                            }
                            openList.push(neighbours[i])
                        }
                        else
                            openList[neighbourIndex] = neighbours[i]
                    }
            }
        }

        else {
            if (currentCell == null)
                currentCell = mat[end[0]][end[1]].parent
            if (currentCell == null)
                clearInterval(timeId)
            if (currentCell) {
                console.log("form interval");
                currentCell.colour = "red"
                currentCell.draw()
                currentCell = currentCell.parent
                if (currentCell.parent == currentCell)
                    clearInterval(timeId)
            }
        }
    }, 20);

}

function biDirectional() {

    for (let i = 0; i < numOfRow; ++i)
        for (let j = 0; j < numOfCol; ++j) {
            mat[i][j].vis = false;
            if (mat[i][j].status)
                mat[i][j].addNeighbours(mat);
        }

    openList[0].f = openList[0].g * gMultiple

    console.log("hello from bi")


    let matCopy = new Array(numOfRow)

    for (let i = 0; i < numOfRow; ++i)
        matCopy[i] = new Array(numOfCol)


    for (let i = 0; i < matCopy.length; i++)  // 1
        for (let j = 0; j < matCopy[i].length; ++j) {
            matCopy[i][j] = new Cell(mat[i][j].i, mat[i][j].j, mat[i][j].colour, Infinity, mat[i][j].status)
            matCopy[i][j].vis = false;
        }

    for (let i = 0; i < numOfRow; ++i)
        for (let j = 0; j < numOfCol; ++j)
            if (matCopy[i][j].status) {
                matCopy[i][j].addNeighbours(matCopy);
            }

    matCopy[start[0]][start[1]].status = true
    matCopy[end[0]][end[1]].parent = matCopy[end[0]][end[1]]
    matCopy[end[0]][end[1]].g = 0

    let openListT = []
    openListT.push(matCopy[end[0]][end[1]])
    openListT[0].f = openListT[0].g * gMultiple


    let currentCellS = null
    let currentCellT = null
    let timeId
    let flag = true

    mat[start[0]][start[1]] = true;
    matCopy[end[0]][end[1]] = true;


    timeId = setInterval(() => {
        if (openListT[0] && openList[0] && flag) { //matCopy[start[0]][start[1]].status

            console.log("hello");
            let indexT = 0 //1
            let index = 0  //2

            for (let i in openListT) //1
                if (openListT[indexT].f > openListT[i].f)
                    indexT = i

            for (let i in openList) //2
                if (openList[index].f > openList[i].f)
                    index = i

            let tempCellT = openListT[indexT] // 1
            let neighboursT = tempCellT.neighbours

            let tempCell = openList[index] //2
            let neighbours = tempCell.neighbours

            openListT.splice(indexT, 1) // 1
            tempCellT.status = false

            openList.splice(index, 1) // 2
            tempCell.status = false

            if (tempCellT.colour != "#00008B") { // 1
                tempCellT.colour = "#ade6d8"
                tempCellT.draw()
            }

            if (tempCell.colour != "green") {  // 2
                tempCell.colour = "#ade6d8"
                tempCell.draw()
            }

            for (let i = 0; i < neighboursT.length && flag; ++i) { // 1
                if (neighboursT[i].status)
                    if (neighboursT[i].g > tempCellT.g + 1) {
                        neighboursT[i].g = tempCellT.g + 1
                        neighboursT[i].f = neighboursT[i].g * gMultiple


                        neighboursT[i].parent = tempCellT

                        let neighbourIndex = openListT.findIndex(item => (item.i == neighboursT[i].i && item.j == neighboursT[i].j))
                        if (neighbourIndex == -1) {
                            if (neighboursT[i].colour != "green") {
                                neighboursT[i].colour = "#add8e6"
                                neighboursT[i].draw()
                            }
                            neighboursT[i].vis = true
                            if (mat[neighboursT[i].i][neighboursT[i].j].vis) {
                                currentCellS = mat[neighboursT[i].i][neighboursT[i].j].parent
                                currentCellT = tempCellT
                                flag = false
                            }

                            openListT.push(neighboursT[i])

                        }
                        else
                            openListT[neighbourIndex] = neighboursT[i]
                    }
            }


            for (let i = 0; i < neighbours.length && flag; ++i) {
                if (neighbours[i].status)
                    if (neighbours[i].g > tempCell.g + 1) {
                        neighbours[i].g = tempCell.g + 1
                        neighbours[i].f = neighbours[i].g * gMultiple


                        neighbours[i].parent = tempCell

                        let neighbourIndex = openList.findIndex(item => (item.i == neighbours[i].i && item.j == neighbours[i].j))
                        if (neighbourIndex == -1) {
                            if (neighbours[i].colour != "00008B") {
                                neighbours[i].colour = "#add8e6"
                                neighbours[i].draw()
                            }
                            neighbours[i].vis = true
                            if (matCopy[neighbours[i].i][neighbours[i].j].vis) {
                                currentCellT = matCopy[neighbours[i].i][neighbours[i].j].parent
                                currentCellS = tempCell
                                flag = false
                            }
                            openList.push(neighbours[i])
                        }
                        else
                            openList[neighbourIndex] = neighbours[i]
                    }
            }
        }

        else {
            if (currentCellS == null || currentCellT == null) {
                console.log(currentCellT)
                clearInterval(timeId)
            }

            else if (currentCellS != currentCellS.parent || currentCellT != currentCellT.parent) {
                console.log("form interval");
                if (currentCellS != currentCellS.parent) {
                    currentCellS.colour = "red"
                    currentCellS.draw()
                    currentCellS = currentCellS.parent
                }

                if (currentCellT != currentCellT.parent) {
                    currentCellT.colour = "red"
                    currentCellT.draw()
                    currentCellT = currentCellT.parent
                }
            }
            else
                clearInterval(timeId)
        }
    }, 20);

}


function randomFill() {
    for (let i = 0; i < numOfRow; ++i) {
        for (let j = 0; j < numOfCol; ++j) {
            if (mat[i][j].colour == "green" || mat[i][j].colour == "#00008B") continue;
            if (Math.random() < 0.2) {
                mat[i][j].colour = "black"
                mat[i][j].status = false
                mat[i][j].draw()
            }
        }
    }


}
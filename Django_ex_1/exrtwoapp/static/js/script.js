alert("The legends say, the design, indeed, was not fancy...");

// Event Listener for <p> elements
document.querySelectorAll('p').forEach(p => {
    p.addEventListener('mousemove', (e) => {
        animateWordsNearCursor(e, p);
    });
});

// Function to animate words near the cursor
function animateWordsNearCursor(event, paragraphElement) {
    let words = getNearestWords(event, paragraphElement);

    // Create a copy of the innerHTML to manipulate
    let newHtml = paragraphElement.innerHTML;

    words.forEach(word => {
        let wordElement = createWordElement(word);
        document.body.appendChild(wordElement);

        // Replace the word in the paragraph with a placeholder
        newHtml = replaceWordWithPlaceholder(newHtml, word);

        // Position element near the cursor and animate
        positionAndAnimateWord(wordElement, event.clientX, event.clientY, paragraphElement, word);
    });

    // Update the paragraph's innerHTML in one go
    paragraphElement.innerHTML = newHtml;
}

// Function to replace a word in the HTML with a placeholder
function replaceWordWithPlaceholder(html, word) {
    let placeholder = `<span class="word-placeholder">${word}</span>`;
    return html.replace(word, placeholder);
}

// Function to position and animate the word
function positionAndAnimateWord(element, x, y, paragraphElement, word) {
    // Set initial position
    element.style.left = `${x}px`;
    element.style.top = `${y}px`;

    // Randomize animation
    let randomX = Math.random() * 100 - 50; // Random X offset
    let randomY = Math.random() * 100 - 50; // Random Y offset

    // Apply animation
    setTimeout(() => {
        element.style.transform = `translate(${randomX}px, ${randomY}px)`;
        // Remove element after animation and return word to paragraph
        setTimeout(() => {
            element.remove();
            returnWordToParagraph(paragraphElement, word);
        }, 500);
    }, 50);
}

// Function to return the word to the paragraph
function returnWordToParagraph(paragraphElement, word) {
    let html = paragraphElement.innerHTML;
    paragraphElement.innerHTML = html.replace(`<span class="word-placeholder">${word}</span>`, word);
}

// Function to get nearest words within a 50-pixel radius
function getNearestWords(event, paragraphElement) {
    const words = paragraphElement.innerText.split(/\s+/);
    const rect = paragraphElement.getBoundingClientRect();
    const cursorX = event.clientX - rect.left; // X position within the element.
    const cursorY = event.clientY - rect.top;  // Y position within the element.
    const radius = 50;
    let nearestWords = [];

    let approxX = 0; // Approximate X position of the current word
    let approxY = 0; // Approximate Y position of the current word
    let lineHeight = parseInt(getComputedStyle(paragraphElement).lineHeight);

    for (let word of words) {
        const wordWidth = ctx.measureText(word).width;
        if (approxX + wordWidth > paragraphElement.clientWidth) {
            approxX = 0;
            approxY += lineHeight;
        }

        if (isWithinRadius(approxX, approxY, cursorX, cursorY, radius)) {
            nearestWords.push(word);
        }

        approxX += wordWidth + ctx.measureText(' ').width; // Add space width
    }

    return nearestWords;
}

function isWithinRadius(wordX, wordY, cursorX, cursorY, radius) {
    const dx = cursorX - wordX;
    const dy = cursorY - wordY;
    return dx * dx + dy * dy <= radius * radius;
}

function createWordElement(word) {
    let element = document.createElement('div');
    element.classList.add('flying-word');
    element.textContent = word;
    return element;
}

// Canvas context for measuring text width
let ctx = document.createElement('canvas').getContext('2d');
ctx.font = getComputedStyle(document.querySelector('p')).font;

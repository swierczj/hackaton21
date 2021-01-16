const errorData = [ { "errorName": "error: incompatible types: String cannot be converted to int", "answers": [ { "url": "https://stackoverflow.com/questions/48347958/error-incompatible-types-string-cannot-be-converted-to-int/48348316", "answerContent": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", "votes": 642, "author": "Maciek69" }, { "url": "https://stackoverflow.com/questions/45450337/incompatible-types-string-cannot-be-converted-to-int", "answerContent": "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here',", "votes": 1337, "author": "Jan Pawel II" }, { "url": "https://stackoverflow.com/questions/48536811/error-incompatible-types-string-cannot-be-converted-to-int-in-java", "answerContent": "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the", "votes": 420, "author": "Marcin Czerwonka" }, { "url": "https://stackoverflow.com/questions/60407041/incompatible-types-java-lang-string-cannot-be-converted-to-int", "answerContent": "Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.", "votes": 69, "author": "Szewczyk Panewka" }, { "url": "https://stackoverflow.com/questions/47396751/incompatible-types-string-cannot-be-converted-to-int-even-therere-no-strings", "answerContent": "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of de Finibus Bonorum", "votes": -9,"author": "Maciek"}]}]


const stackIconUrl = "https://img.icons8.com/color/96/000000/stackoverflow.png"

const createErrorPanel = (postAuthor, content, votes, url, i) => {  
  // creating elements
  let errorContainer = document.createElement("div")
  errorContainer.setAttribute('class', 'errorContainer')

  let errorHeader = document.createElement('div')
  errorHeader.setAttribute('class', 'errorContainer__errorHeader')
  
  let headerImg = document.createElement('img')
  headerImg.setAttribute('src', stackIconUrl)
  headerImg.setAttribute('width', '50px')
  headerImg.setAttribute('height', '50px')

  let headerParagraphsContainer = document.createElement('div')
  headerParagraphsContainer.setAttribute('class', 'flxbox flxbox--column flxbox--alignStart')

  let errorDetails = document.createElement('div')
  errorDetails.setAttribute('class', 'errorContainer__errorDetails')
  
  let paragraphBestAnswear = document.createElement('p')
  paragraphBestAnswear.setAttribute('class', 'fontLarge primaryText bold')
  
  let paragraphAuthor = document.createElement('p')
  paragraphAuthor.setAttribute('class', 'fontLarge')
  
  let answearContent = document.createElement('div')
  answearContent.setAttribute('class', 'answear pad')
  
  let paragraphVotes = document.createElement('p')
  paragraphVotes.setAttribute('class', 'primaryText bold')

  let buttonContainer = document.createElement('div')
  buttonContainer.setAttribute('class', 'flxbox')

  let anchorButton = document.createElement('a')
  anchorButton.setAttribute('class', 'button debug')
  anchorButton.setAttribute('href', url)

  // setting inner html
  
  paragraphBestAnswear.innerHTML = "Best Answer"
  paragraphAuthor.innerHTML = `User: ${postAuthor}`
  answearContent.innerHTML = content
  paragraphVotes.innerHTML = `${votes} votes`
  
  anchorButton.innerHTML = "check thread"
  
  headerParagraphsContainer.appendChild(paragraphBestAnswear)
  headerParagraphsContainer.appendChild(paragraphAuthor)

  errorHeader.appendChild(headerImg)
  errorHeader.appendChild(headerParagraphsContainer)

  errorDetails.appendChild(answearContent)
  errorDetails.appendChild(paragraphVotes)
  buttonContainer.appendChild(anchorButton)
  errorDetails.appendChild(buttonContainer)

  errorContainer.appendChild(errorHeader)
  errorContainer.appendChild(errorDetails)

  document.getElementById(`errorContainer${i}`).appendChild(errorContainer)
}

errorData.forEach((value, i) => {
  console.log(value, i)
  let errorContainer = document.createElement('div')
  errorContainer.setAttribute('class', 'flxbox flxbox--wrap')
  errorContainer.setAttribute('id', `errorContainer${i}`)
  let errorName = document.createElement('h3')
  errorName.innerHTML = value.errorName
  errorContainer.appendChild(errorName)
  document.getElementById("errorsContainer").appendChild(errorContainer)
  value.answers.forEach(answer => createErrorPanel(answer.author, answer.answerContent, answer.votes, answer.url, i))
})

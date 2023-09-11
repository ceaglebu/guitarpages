class Existing {
    constructor(id, length) {
        this.id = id
        this.length = length
    }
}

class Fresh {
    constructor(name, type, quality_measurement, description, skills, video_link, privacy) {
        this.name = name
        this.type = type
        this.quality_measurement = quality_measurement
        this.description = description
        this.skills = skills
        this.video_link = video_link
        this.privacy = privacy
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const add_exercise_div = document.querySelector('#add-exercise-div')
    const add_new_btn = document.querySelector('#add-new-exercise')
    const add_existing_btn = document.querySelector('#add-existing-exercise')

    let exercises = []

    let hide_add_exercise_buttons = () => {
        add_new_btn.style.display = 'none'
        add_existing_btn.style.display = 'none'        
    }

    let hide_add_exercise_form = () => {
        add_exercise_div.innerHTML = ''
    }

    let show_add_exercise_buttons = () => {
        add_new_btn.style.display = 'inline-block'
        add_existing_btn.style.display = 'inline-block'        
    }

    let reset_buttons = () => {
        hide_add_exercise_form()
        show_add_exercise_buttons()
    }

    // onclick function for adding exercise
    let add_exercise = () => {
        exercises.push(
            new Existing(document.querySelector('#exercise').value, document.querySelector('#length').value)
        )
        reset_buttons()
        console.log(exercises)
        return false
    }

    add_new_btn.onclick = () => {
        // Hide buttons
        hide_add_exercise_buttons()

        // Load form for creating exercise
        fetch('/components/new_exercise')
        .then(response => response.json())
        .then(response => {
            add_exercise_div.innerHTML = response.body

            document.querySelector('#add-exercise-btn').onclick = add_exercise
            document.querySelector('#cancel-add-btn').onclick = reset_buttons
        })
        
        return false
    }
    
    add_existing_btn.onclick = () => {
        // Hide buttons
        hide_add_exercise_buttons()
        
        // Load form for choosing exercise
        fetch('/components/add_exercise')
        .then(response => response.json())
        .then(response => {
            // Add error handling here
            add_exercise_div.innerHTML = response.body

            document.querySelector('#add-exercise-btn').onclick = add_exercise
            document.querySelector('#cancel-add-btn').onclick = () => {
                hide_add_exercise_form()
                show_add_exercise_buttons()
            }
        })

        return false
    }
})
function calculateBMI() {
    // Get the values from the input fields
    const weight = parseFloat(document.getElementById('weight').value);
    const height = parseFloat(document.getElementById('height').value);
    const heightUnit = document.getElementById('heightUnit').value;
    const age = parseInt(document.getElementById('age').value);
    const gender = document.querySelector('input[name="gender"]:checked').value;

    // Check if the inputs are valid
    if (isNaN(weight) || isNaN(height) || isNaN(age) || height <= 0 || age <= 0) {
        alert("Please enter valid weight, height, and age.");
        return;
    }

    // Convert height to meters if needed
    let heightInMeters;
    if (heightUnit === "cm") {
        heightInMeters = height / 100; // Convert cm to meters
    } else {
        heightInMeters = height * 0.3048; // Convert feet to meters
    }

    const bmi = (weight / (heightInMeters * heightInMeters)).toFixed(2);
    document.getElementById('result').value = bmi;

   
    categorizeBMI(bmi, weight, age, gender);
}



function calculateCalories(weight, age, gender) {
    let bmr;

    // Harris-Benedict equation
    if (gender === "male") {
        bmr = 88.362 + (13.397 * weight) + (4.799 * 176) + (5.677 * age);
    } else {
        bmr = 447.593 + (9.247 * weight) + (3.098 * 176) + (4.330 * age);
    }

    // Assuming a sedentary lifestyle (BMR * 1.2)
    const dailyCalories = bmr * 1.2;
    return dailyCalories;
}

function resetForm() {
    document.getElementById('bmiForm').reset();
    document.getElementById('result').value = "";
    document.getElementById('calorieResult').value = "";
    document.getElementById("dietPlan").style.display = "none"
}

function categorizeBMI(bmi, weight, age, gender) {
    let category = "";

if(bmi>29.9){
category = "Obesity"
}else if (bmi < 18.5) {
        category = "Underweight";
    } else if (bmi >= 18.5 && bmi < 24.9) {
        category = "Normalweight";
    } else if (bmi >= 25 && bmi < 29.9) {
        category = "Overweight";
    } else {
return
    }

    const calories = calculateCalories(weight, age, gender);
    document.getElementById('calorieResult').value = `You should consume approximately ${calories.toFixed(0)} calories per day.`;

const result = document.getElementById('result').value
document.getElementById('result').value = `${result}.... You Are In ${category}`

    document.getElementById("dietPlan").style.display = "block"


    const dietCategory = ["Obesity", "Underweight", "Normalweight", "Overweight"]

    dietCategory.map((item) => (
        item != category ?  document.getElementById(item).style.display = "none" : document.getElementById(item).style.display = "block"
    ))

    console.log("done")
}
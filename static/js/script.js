fetch("/config")
    .then( r => r.json())
    .then(({personalPlan, familyPlan}) => {
        const personalPlanInput = document.querySelector('#personalPlan');
        personalPlanInput.value = personalPlan;
        const familyPlanInput = document.querySelector('#familyPlan');
        familyPlanInput.value = familyPlan;
    })
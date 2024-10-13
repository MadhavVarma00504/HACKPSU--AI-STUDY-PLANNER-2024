$(document).ready(function() {
    // Add Task Button
    $('#addTaskBtn').click(function(event) {
        event.preventDefault();
        const taskData = {
            task_name: $('#task_name').val(),
            deadline: $('#deadline').val(),
            duration: $('#duration').val(),
            priority: $('#priority').val()
        };
        
        $.ajax({
            url: '/add_task',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(taskData),
            success: function(response) {
                alert('Task added successfully');
                // Optionally, update calendar or task list here
            }
        });
    });

    // Set Free Time Button
    $('#setFreeTimeBtn').click(function(event) {
        event.preventDefault();
        const freeTimeData = {
            free_time_start: $('#free_time_start').val(),
            free_time_end: $('#free_time_end').val()
        };

        $.ajax({
            url: '/set_free_time',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(freeTimeData),
            success: function(response) {
                $('#recommendedTimes').empty();
                response.predicted_times.forEach(function(item) {
                    $('#recommendedTimes').append(`<p>Time: ${item.time}:00, Productivity Score: ${item.productivity_score}</p>`);
                });
            }
        });
    });
});

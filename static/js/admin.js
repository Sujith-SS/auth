$(document).ready(function() {
    // Show user details by default
    $('#addUserForm').show();

    // Toggle between user details and create user form
    $('#users-link').click(function() {
        $('.form-container').hide();
        $('#addUserForm').show();
    });

    // Show the create user form when the link is clicked
    $('#create-user-link').click(function() {
        $('.form-container').hide();
        $('#createUserForm').show();
    });

    // Submit the form to create a new user
    $('#new-user-form').submit(function(event) {
        event.preventDefault();
       
    });
});

// JavaScript/jQuery code to toggle modals

$(document).ready(function() {
    // When the edit button is clicked, show the edit user modal
    $('.btn-edit').click(function() {
        $('#editUserModal').modal('show');
    });
});
// Toggle between user details and create user form
$('#users-link').click(function() {
    $('.form-container').hide();
    $('#addUserForm').show();
});

// Show the create user form when the link is clicked
$('#create-user-link').click(function() {
    $('.form-container').hide();
    $('#createUserForm').show();
});

// Submit the form to create a new user
$('#new-user-form').submit(function(event) {
    event.preventDefault();
   
});


// JavaScript/jQuery code to toggle modals

$(document).ready(function() {
// When the edit button is clicked, show the edit user modal
$('.btn-edit').click(function() {
    $('#editUserModal').modal('show');
});
});
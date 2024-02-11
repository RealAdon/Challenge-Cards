$(document).ready(function(){
    let selectedCard = null;

    // Delegate card clicks from the #hand section
    $('#hand').on('click', '.card', function() {
        $(".card").removeClass('selected'); // Deselect any previously selected card
        $(this).addClass('selected'); // Select this card
        selectedCard = $(this).data('card');
    });

    // Delegate pile clicks from the #piles section
    $('#piles').on('click', '.pile', function() {
        if (selectedCard !== null) {
            let pile = $(this).data('pile');
            $.ajax({
                url: '/play_card',
                type: 'POST',
                data: {card: selectedCard, pile: pile},
                success: function(response){
                    if (response.success) {
                        $('.card.selected').remove(); // Remove the selected card from the hand
                        $(`.pile[data-pile="${pile}"]`).text(selectedCard); // Update the text of the pile
                        selectedCard = null; // Reset selectedCard
                    } else {
                        alert("Move not allowed");
                    }
                }
            });
        }
    });
    // Handler for the Draw Cards button
    $(".draw_cards_button").click(function() {
        $.ajax({
            url: '/draw_cards',
            type: 'GET',
            success: function(response) {
                // Assuming the response contains the updated hand
                if(response.success) {
                    // Update the hand display based on the response
                    // This part requires you to adjust based on how you want to display the updated hand
                    $('#hand').empty(); // Clear current hand display
                    response.hand.forEach(function(card) {
                        // Append each new card to the hand display
                        $('#hand').append('<div class="card" data-card="' + card + '">' + card + '</div>');
                    });
                    // Re-bind click event to new card elements if necessary
                } else {
                    alert("Could not draw cards");
                }
            },
            error: function(xhr, status, error) {
                // Handle any errors here
                console.error("Error drawing cards: ", status, error);
            }
        });
    });
});
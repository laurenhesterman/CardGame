class Deck {
    constructor(cards) {
        this.cards = cards
        
    }
    showsdeck() {
        console.log(cards)
    }
    shuffle() {
        for (let i = cards.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [cards[i], cards[j]] = [cards[j], cards[i]];
        }
        return cards;
    }
    reset() {
        cards = [];
        for (var i=1; i<5; i++){
            for (var k=1; k<14; k++) {
                card = "";
                card += i;
                card += k;
                cards.push(card)
            }
        }
    }
    dealrandom(x) {
        var index = Math.floor(Math.random()*52)
        console.log(cards[index])
        x.hand.push(cards[index])
        cards.splice(index, 1)
    }
  

}
class Player {
    constructor(name, hand=[]) {
        this.name = name;
        this.hand = hand;     
    }
    showshand() {
        console.log(this.hand)
    }
}




var cards = [];
for (var i=1; i<5; i++){
            for (var k=1; k<14; k++) {
                card = "";
                card += i;
                card += k;
                cards.push(card)
            }
        }



const deck1 = new Deck(cards);
deck1.showsdeck();
deck1.shuffle();
deck1.showsdeck();
deck1.reset();
deck1.showsdeck();
const player1 = new Player("Lauren");
player1.showshand();
deck1.dealrandom(player1);
player1.showshand();

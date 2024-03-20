pragma solidity ^0.5.0;

contract Voting {
    struct Candidate {
        string name;
        uint voteCount;
    }

    mapping(address => bool) public voters;
    Candidate[] public candidates;
    uint public totalVoters;

    constructor(string[] memory candidateNames) public {
        for (uint i = 0; i < candidateNames.length; i++) {
            candidates.push(Candidate({
                name: candidateNames[i],
                voteCount: 0
            }));
        }
    }

    function registerVoter(address voterAddress) public {
        require(!voters[voterAddress], "You have already registered.");
        voters[voterAddress] = true;
        totalVoters++;
    }

    function vote(uint candidate) public {
        require(voters[msg.sender], "You must be a registered voter to vote.");
        require(candidate < candidates.length, "Invalid candidate.");

        candidates[candidate].voteCount++;
    }

    function getWinner() public view returns (string memory) {
        uint maxVotes = 0;
        uint winningCandidate = 0;
        for (uint i = 0; i < candidates.length; i++) {
            if (candidates[i].voteCount > maxVotes) {
                maxVotes = candidates[i].voteCount;
                winningCandidate = i;
            }
        }
        return candidates[winningCandidate].name;
    }

    function getCandidates() public view returns (string[] memory) {
        string[] memory candidateNames = new string[](candidates.length);
        for (uint i = 0; i < candidates.length; i++) {
            candidateNames[i] = candidates[i].name;
        }
        return candidateNames;
    }
}
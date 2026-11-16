
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    // Structure
    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    // Array
    Student[] public students;

    // Add student data
    function addStudent(
        uint _rollNo,
        string memory _name,
        uint _marks
    ) public {
        students.push(Student(_rollNo, _name, _marks));
    }

    // Get student data
    function getStudent(uint index)
        public view returns (uint, string memory, uint) {

        Student memory s = students[index];

        return (s.rollNo, s.name, s.marks);
    }

    // Get total students
    function getCount() public view returns (uint) {
        return students.length;
    }

    // Fallback function
    fallback() external payable {
    }
}

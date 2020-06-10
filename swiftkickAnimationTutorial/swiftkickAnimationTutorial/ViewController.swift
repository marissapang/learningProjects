//
//  ViewController.swift
//  swiftkickAnimationTutorial
//
//  Created by apple on 6/10/20.
//  Copyright © 2020 KnowledgeIsBacon. All rights reserved.
//

import UIKit

enum AnimationDirection: Int {
    case up, down, left, right, undefined
}

class ViewController: UIViewController {
    var animator = UIViewPropertyAnimator()
    @IBOutlet weak var squareView: UIView!
    
    
    @objc private func handlePan(recognizer: UIPanGestureRecognizer) {
        // print(directionFromVelocity(recognizer.velocity(in: squareView)))
        var direction : AnimationDirection
        let animationSize : CGFloat = 100
        var directionalSize : CGFloat
        
        switch recognizer.state {
        case .began:
            direction = directionFromVelocity(recognizer.velocity(in: squareView))
            print(direction)
            switch direction {
            case .right:
                directionalSize = animationSize
            case .left:
                directionalSize = -animationSize
            default:
                directionalSize = animationSize
            }
            animator = UIViewPropertyAnimator(duration: 1, curve: .easeInOut, animations: {
                self.squareView.transform = CGAffineTransform(translationX: directionalSize, y: 0)
                self.squareView.alpha = 1
            })
            animator.startAnimation()
            animator.pauseAnimation()
        case .changed:
            direction = directionFromVelocity(recognizer.velocity(in: squareView))
            animator.fractionComplete = abs(recognizer.translation(in: squareView).x) / animationSize
            print(animator.fractionComplete)
        case .ended:
            if animator.fractionComplete < 0.1 {
                animator.isReversed = true
            } else {
                animator.isReversed = false
            }
            animator.continueAnimation(withTimingParameters: nil, durationFactor: 0)
        default:
            ()
        }
        
    }
    
    private func directionFromVelocity(_ velocity: CGPoint) -> AnimationDirection {
        guard velocity != .zero else { return .undefined }
        let isVertical = abs(velocity.y) > abs(velocity.x)
        var derivedDirection: AnimationDirection = .undefined
        if isVertical {
            derivedDirection = velocity.y < 0 ? .up : .down
        } else {
            derivedDirection = velocity.x < 0 ? .left : .right
        }
        return derivedDirection
    }
    
    private lazy var panRecognizer: UIPanGestureRecognizer = {
        let recognizer = UIPanGestureRecognizer()
        recognizer.addTarget(self, action: #selector(handlePan(recognizer:)))
        return recognizer
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        squareView.addGestureRecognizer(panRecognizer)
    }


}

